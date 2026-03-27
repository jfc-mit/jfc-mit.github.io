import urllib.request
import urllib.error
import time

repos = [
    "analysis_zlineshape_alpha_s",
    "analysis_lund_plane",
    "analysis_eec_correlators",
    "analysis_rb_rc",
    "z-counting-nnu-delphi",
    "lund-plane-delphi",
    "had-eventshape-alphas-delphi",
    "jet-substructure-delphi",
    "higgstautau-cms-opendata"
]

branches = ["main", "master"]
folders = [
    "analysis_note",
    "phase5_documentation/outputs",
    "phase5_documentation/exec",
    "phase4_inference/outputs",
    "phase4_inference/4c_observed/outputs",
    "phase4_inference/4b_partial/outputs",
    "phase4_inference/exec"
]
prefixes = ["ANALYSIS_NOTE_doc4c_v", "ANALYSIS_NOTE_5_v", "ANALYSIS_NOTE_4c_v"]

print("Starting HTTP scan against raw.githubusercontent.com...", flush=True)

success_mapping = {}

for repo in repos:
    found = False
    for branch in branches:
        if found: break
        for folder in folders:
            if found: break
            for prefix in prefixes:
                if found: break
                for v in range(5, 0, -1):
                    # test the versioned file and exactly "ANALYSIS_NOTE.pdf"
                    filenames = [f"{prefix}{v}.pdf", f"ANALYSIS_NOTE_doc4b_v{v}.pdf", "ANALYSIS_NOTE.pdf"]
                    for filename in filenames:
                        url = f"https://raw.githubusercontent.com/jfc-mit/{repo}/{branch}/{folder}/{filename}"
                        try:
                            # Use HEAD to quickly check existence
                            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
                            res = urllib.request.urlopen(req)
                            if res.status == 200:
                                result = f"blob/{branch}/{folder}/{filename}"
                                print(f"[OK] {repo} -> {result}", flush=True)
                                success_mapping[repo] = result
                                found = True
                                break
                        except urllib.error.HTTPError:
                            pass
                        except Exception as e:
                            print(e)
    if not found:
        print(f"[FAIL] Could not find any PDF for {repo}", flush=True)

print("Scan complete.", flush=True)
