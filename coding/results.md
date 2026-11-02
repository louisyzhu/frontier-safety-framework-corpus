# Results (readj codes), sheet tracing_FINAL_v3.csv, rows 710, material 480

## RQ1 pooled (8 accounted pairs): strict 252/392 = 0.643 CI (0.5942469419047952, 0.6886945175072525); lenient 118/392 = 0.301 CI (0.2577219859484663, 0.3481809812990388)
evidentiary: strict 160/262 = 0.611, lenient 0.294; non-evidentiary strict 0.708, lenient 0.315
per pair strict (min/max over accounted pairs): ANT-1 0.56, ANT-2 0.67, OAI-1 0.57, GDM-1 0.75, GDM-2 0.48, META-1 0.67, MSFT-1 0.86, NAV-1 0.71
per pair intervals strict: Anthropic 1.0→2.0 0.56 (0.45, 0.66); Anthropic 2.2→3.0 0.67 (0.57, 0.76); OpenAI Beta→2 0.57 (0.42, 0.71); DeepMind 2.0→3.0 0.75 (0.58, 0.87); DeepMind 3.0→3.1 0.48 (0.31, 0.66); Meta 1.1→2 0.67 (0.56, 0.76); Microsoft v1→2026 0.86 (0.65, 0.95); Naver 2024→2.0 0.71 (0.51, 0.85)
per pair intervals lenient: Anthropic 1.0→2.0 0.15 (0.09, 0.25); Anthropic 2.2→3.0 0.31 (0.23, 0.42); OpenAI Beta→2 0.24 (0.13, 0.39); DeepMind 2.0→3.0 0.41 (0.26, 0.58); DeepMind 3.0→3.1 0.11 (0.04, 0.28); Meta 1.1→2 0.42 (0.32, 0.53); Microsoft v1→2026 0.62 (0.41, 0.79); Naver 2024→2.0 0.25 (0.12, 0.45)
provider aggregates strict: OpenAI 0.57 (24/42), Anthropic 0.62 (102/165), Google DeepMind 0.63 (37/59), Meta 0.67 (54/81), Naver 0.71 (17/24), Microsoft 0.86 (18/21)

## Section granularity: 170 units; strict 84/170 = 0.49 CI (0.41992521942135747, 0.5685700544371436); lenient 34/170 = 0.20 CI (0.1467991020988553, 0.26645986468469934); majority rule 0.58

## RQ2: narrative strict 99/142 = 0.697 CI (0.6172359313103976, 0.7667423026091424); itemised 153/250 = 0.612 CI (0.550334217662286, 0.6702758005537984); Fisher OR 1.46 p = 0.100
lenient: narrative 46/142 = 0.324, itemised 72/250 = 0.288; OR 1.18 p = 0.492
permutation (56 assignments): observed pooled diff 0.085, p = 0.125; per-pair mean diff 0.084, p = 0.179
Spearman strict rate vs words -0.24, items -0.58, words/change 0.10, items/change -0.13

## RQ3: weakening share 230/306 = 0.752 CI (0.7003030080879232, 0.7967251508164976)
excluding MIX (54): 177/252 = 0.702 CI (0.6432340488314628, 0.7554501370085256)
excluding L: 222/298 = 0.745
outcomes among material: {'W': 178, 'S': 77, 'X': 44, 'A': 173, 'L': 8}; additions 173
additions by pair: {'ANT-1': 22, 'ANT-2': 26, 'GDM-1': 9, 'GDM-2': 11, 'META-1': 57, 'MSFT-1': 8, 'NAV-1': 9, 'OAI-1': 10, 'XAI-2': 7, 'XAI-3': 5, 'XAI-4': 10}
pairs with weakening majority: 9 of 12; per pair: ANT-1 0.82, ANT-2 0.93, OAI-1 0.94, GDM-1 0.74, GDM-2 0.38, META-1 0.46, MSFT-1 0.69, NAV-1 0.73, XAI-1 1.00, XAI-2 0.63, XAI-3 0.25, XAI-4 0.71
leave-one-provider-out: Anthropic 127/189 = 0.67, Google DeepMind 207/267 = 0.78, Meta 219/282 = 0.78, Microsoft 221/293 = 0.75, Naver 219/291 = 0.75, OpenAI 200/274 = 0.73, xAI 187/240 = 0.78
strict silence: weakenings 130/187 = 0.695, strengthenings 28/54 = 0.519, OR 2.12 p = 0.022; additions 94/151 = 0.623
by outcome strict silence: W 101/148, X 23/31, L 6/8, S 28/54, A 94/151
lenient silence: weakenings 61/187 = 0.326, strengthenings 16/54 = 0.296, OR 1.15 p = 0.742
within-pair strict silence W vs S: ANT-1 0.45 vs 0.60 (47/10); ANT-2 0.77 vs 0.75 (56/4); OAI-1 0.63 vs 0.50 (30/2); GDM-1 1.00 vs 0.57 (17/7); GDM-2 1.00 vs 0.20 (6/10); META-1 0.55 vs 0.46 (11/13); MSFT-1 0.89 vs 0.75 (9/4); NAV-1 0.91 vs 0.75 (11/4)
pairs with weakenings more often silent: 7 of 8; margins ANT-1 -0.15, ANT-2 +0.02, OAI-1 +0.13, GDM-1 +0.43, GDM-2 +0.80, META-1 +0.08, MSFT-1 +0.14, NAV-1 +0.16

## TFAIA split (accounted): before strict 92/153 = 0.60, lenient 0.23; after strict 160/239 = 0.67, lenient 0.35
weakening share all pairs: before 113/144 = 0.78, after 117/162 = 0.72

## categories strict intervals: EC1 (0.30, 0.64), EC2 (0.47, 0.71), EC3 (0.60, 0.82), EC4 (0.36, 0.78), EC5 (0.54, 0.81), EC6 (0.40, 0.65), G (0.66, 0.86), S (0.38, 0.72), M (0.54, 0.83)
EC2 material 69; EC4 material 20, with account 17, strict silent 10/17

## Re-adjudication: 249 rows re-examined; materiality changed 19; outcome changed 43; announcement changed 125: {('SIL', 'ANN-P'): 84, ('ANN-P', 'ANN'): 10, ('NA', 'ANN-P'): 7, ('NA', 'ANN'): 2, ('NA', 'SIL'): 4, ('SIL', 'ANN'): 5, ('ANN', 'ANN-P'): 3, ('SIL', 'NA'): 4, ('ANN-P', 'SIL'): 4, ('NCL', 'NA'): 2}
first pass -> adjudication: outcome {('R', 'S'): 2, ('X', 'L'): 1, ('S', 'W'): 1}, announcement {('SIL', 'ANN-P'): 46, ('NA', 'SIL'): 1, ('ANN', 'ANN-P'): 8, ('NA', 'NCL'): 1}
