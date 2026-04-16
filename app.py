import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Color Memory Game", layout="wide")

st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxmuZRNR9qR1sFFPe7TMeRrAJo6sBkVSRkmftl-wq5hDMSVOmFbNLzBK_Sfj2QnW6a5/exec"

html = f"""
<style>
input[type=range] {{
  -webkit-appearance: none;
  height: 18px;
  border-radius: 10px;
  outline: none;
}}

input[type=range]::-webkit-slider-runnable-track {{
  height: 18px;
  border-radius: 10px;
}}

input[type=range]::-webkit-slider-thumb {{
  -webkit-appearance: none;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: white;
  cursor: pointer;
  margin-top: -5px;
}}

input[type=range]::-moz-range-track {{
  height: 18px;
  border-radius: 10px;
}}

input[type=range]::-moz-range-thumb {{
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: white;
  cursor: pointer;
}}

.label-row {{
  display: flex;
  justify-content: space-between;
  margin-bottom: 6px;
  font-size: 14px;
  font-weight: 600;
}}

.value-readout {{
  font-family: monospace;
  opacity: 0.9;
}}

.result-swatch {{
  width: 96px;
  height: 96px;
  border-radius: 14px;
  border: 2px solid rgba(255,255,255,0.15);
  box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}}

.result-label {{
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 8px;
  text-align: center;
  color: rgba(255,255,255,0.95);
}}

.summary-card {{
  width: 100%;
  background: #242424;
  border: 1px solid #444;
  border-radius: 14px;
  padding: 16px;
  box-sizing: border-box;
}}

.summary-grid {{
  display: grid;
  grid-template-columns: 74px 1.35fr 1.35fr 90px 90px;
  gap: 12px;
  align-items: center;
}}

.summary-head {{
  font-weight: 700;
  opacity: 0.95;
  font-size: 14px;
}}

.summary-cell {{
  font-size: 14px;
  opacity: 0.95;
}}

.mini-swatch-wrap {{
  display: flex;
  gap: 14px;
  align-items: center;
}}

.mini-swatch-block {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}}

.mini-swatch {{
  width: 42px;
  height: 42px;
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,0.2);
}}

.phase-title {{
  font-size: 24px;
  font-weight: 800;
  margin-bottom: 6px;
  text-align: center;
}}

.phase-subtitle {{
  font-size: 16px;
  opacity: 0.85;
  text-align: center;
}}

.compact-color-line {{
  font-size: 12px;
  opacity: 0.9;
  text-align: center;
  line-height: 1.35;
  white-space: nowrap;
}}

.start-screen {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  margin-top: 140px;
  color: white;
  font-family: sans-serif;
}}

.start-title {{
  font-size: 42px;
  font-weight: 800;
  text-align: center;
}}

.start-subtitle {{
  font-size: 16px;
  opacity: 0.85;
  text-align: center;
}}

.name-input {{
  width: 360px;
  max-width: 90vw;
  padding: 14px 16px;
  font-size: 18px;
  border-radius: 12px;
  border: 1px solid #555;
  background: #1e1e1e;
  color: white;
  outline: none;
  box-sizing: border-box;
}}

.name-input::placeholder {{
  color: rgba(255,255,255,0.45);
}}

.primary-btn {{
  padding: 12px 18px;
  font-size: 16px;
  font-weight: 600;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: white;
  color: black;
}}

.validation-text {{
  min-height: 22px;
  font-size: 14px;
  color: #ff8d8d;
  text-align: center;
}}

.player-name-banner {{
  font-size: 15px;
  font-weight: 600;
  opacity: 0.9;
  text-align: center;
  margin-bottom: 4px;
}}

.download-btn {{
  padding: 12px 18px;
  font-size: 15px;
  font-weight: 600;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: white;
  color: black;
  text-decoration: none;
  display: inline-block;
}}

.download-row {{
  display: flex;
  justify-content: center;
  gap: 14px;
  margin-top: 22px;
  flex-wrap: wrap;
}}

.save-status {{
  margin-top: 14px;
  font-size: 14px;
  opacity: 0.9;
  text-align: center;
  min-height: 20px;
}}
</style>

<div style="font-family:sans-serif; display:flex; flex-direction:column; align-items:center; gap:30px; color:white;">

  <div id="startScreen" class="start-screen">
    <div class="start-title">Color Memory Game</div>
    <div class="start-subtitle">Enter your name to begin</div>
    <input id="playerNameInput" class="name-input" type="text" maxlength="40" placeholder="Your name" />
    <button id="startGameBtn" class="primary-btn">Start Game</button>
    <div id="startValidation" class="validation-text"></div>
  </div>

  <div id="gameContainer" style="display:none; width:100%; flex-direction:column; align-items:center; gap:30px;">
    <div id="countdownPhase" style="
      font-size:140px;
      font-weight:bold;
      margin-top:120px;
    ">3</div>

    <div id="targetPhase" style="display:none; text-align:center; margin-top:30px;">
      <div style="margin-bottom:10px; font-weight:600;">Target</div>
      <div id="targetBox" style="width:300px; height:300px; border-radius:16px; border:2px solid #555;"></div>
    </div>

    <div id="playPhase" style="display:none; flex-direction:column; align-items:center; gap:30px; margin-top:30px;">

      <div id="playerColorSection" style="position:relative; display:flex; justify-content:center; width:300px;">
        <div style="text-align:center;">
          <div style="margin-bottom:10px; font-weight:600;">Your color</div>
          <div id="preview" style="
            width:300px;
            height:300px;
            background:#408080;
            border-radius:16px;
            border:2px solid #555;">
          </div>
        </div>
      </div>

      <div id="controlsSection" style="width:400px; display:flex; flex-direction:column; gap:15px;">
        <div>
          <div class="label-row">
            <label for="h">Hue</label>
            <span id="hValue" class="value-readout">180°</span>
          </div>
          <input
            id="h"
            type="range"
            min="0"
            max="360"
            step="1"
            value="180"
            style="width:100%; background: linear-gradient(to right, red, yellow, lime, cyan, blue, magenta, red);">
        </div>

        <div>
          <div class="label-row">
            <label for="s">Saturation</label>
            <span id="sValue" class="value-readout">50%</span>
          </div>
          <input id="s" type="range" min="0" max="100" step="1" value="50" style="width:100%;">
        </div>

        <div>
          <div class="label-row">
            <label for="v">Brightness</label>
            <span id="vValue" class="value-readout">50%</span>
          </div>
          <input id="v" type="range" min="0" max="100" step="1" value="50" style="width:100%;">
        </div>
      </div>

      <div id="playActionArea" style="display:none; justify-content:center; margin-top:6px;">
        <button id="playActionBtn" class="primary-btn">
          See results
        </button>
      </div>

      <div id="results" style="
        display:none;
        width:500px;
        margin-top:20px;
        padding:22px 18px 18px 18px;
        border-radius:16px;
        background:#1e1e1e;
        border:1px solid #444;
        color:white;
        font-family:sans-serif;
        box-sizing:border-box;
      ">
        <div id="resultsInner" style="
          display:flex;
          flex-direction:column;
          align-items:center;
          width:100%;
        ">
          <div id="roundResultHeading" style="
            font-size:22px;
            font-weight:800;
            text-align:center;
            margin-bottom:14px;
          ">
            Round 1 Results
          </div>

          <div id="scoreDisplay" style="
            font-size:72px;
            font-weight:800;
            text-align:center;
            line-height:1;
            margin-bottom:26px;
            letter-spacing:-1px;
          ">
            Score: <span id="scoreValue">0.00</span>
          </div>

          <div id="colorComparison" style="
            display:flex;
            justify-content:center;
            align-items:flex-start;
            gap:28px;
            width:100%;
            margin-bottom:18px;
          ">
            <div style="
              display:flex;
              flex-direction:column;
              align-items:center;
              width:140px;
            ">
              <div class="result-label">Original</div>
              <div id="targetColorBox" class="result-swatch"></div>
            </div>

            <div style="
              display:flex;
              flex-direction:column;
              align-items:center;
              width:140px;
            ">
              <div class="result-label">Yours</div>
              <div id="playerColorBox" class="result-swatch"></div>
            </div>
          </div>

          <div id="resultsDetails" style="
            display:flex;
            flex-direction:column;
            align-items:center;
            width:100%;
            margin-top:4px;
          ">
            <div style="
              display:flex;
              justify-content:space-between;
              align-items:flex-start;
              width:456px;
            ">
              <div style="
                width:200px;
                text-align:center;
              ">
                <div style="font-weight:700; margin-bottom:8px;">Original color</div>
                <div id="targetInfo"></div>
              </div>

              <div style="
                width:200px;
                text-align:center;
              ">
                <div style="font-weight:700; margin-bottom:8px;">Your choice</div>
                <div id="playerInfo"></div>
              </div>
            </div>

            <div id="timeSpentDisplay" style="
              margin-top:18px;
              font-size:18px;
              font-weight:600;
              text-align:center;
              opacity:0.9;
            ">
              Time spent adjusting: 0.00s
            </div>
          </div>

          <div id="resultsActionArea" style="
            display:none;
            justify-content:center;
            margin-top:22px;
            width:100%;
          ">
            <button id="resultsActionBtn" class="primary-btn">
              Next round
            </button>
          </div>
        </div>
      </div>

      <div id="finalSummary" style="
        display:none;
        width:980px;
        margin-top:20px;
        padding:24px 20px 20px 20px;
        border-radius:16px;
        background:#1e1e1e;
        border:1px solid #444;
        color:white;
        box-sizing:border-box;
      ">
        <div class="phase-title">Final Results</div>
        <div id="playerNameFinal" class="player-name-banner"></div>
        <div class="phase-subtitle" id="finalStats">Total: 0.00 • Average: 0.00</div>

        <div id="summaryRows" style="
          display:flex;
          flex-direction:column;
          gap:14px;
          margin-top:24px;
        "></div>

        <div class="download-row">
          <a id="downloadRoundsBtn" class="download-btn" download="round_level_results.tsv">Download rounds file</a>
          <a id="downloadSessionBtn" class="download-btn" download="game_level_results.tsv">Download game file</a>
        </div>

        <div id="saveStatus" class="save-status"></div>

        <div style="display:flex; justify-content:center; margin-top:24px;">
          <button id="restartBtn" class="primary-btn">
            Play again
          </button>
        </div>
      </div>

    </div>
  </div>
</div>

<script>
const TOTAL_ROUNDS = 5;
const APPS_SCRIPT_URL = {APPS_SCRIPT_URL!r};

let currentRound = 1;
let roundResults = [];
let sessionResults = [];
let targetHSV = randomTargetHSV();
let countdownInterval = null;
let revealTimeout = null;
let adjustStartTime = null;
let playerName = "";
let sessionId = "";
let currentRoundInitialHSV = null;
let currentSessionStartTimestamp = "";
let resultsSaved = false;

function generateSessionId() {{
  return "S_" + Date.now() + "_" + Math.random().toString(36).slice(2, 10);
}}

function nowIso() {{
  return new Date().toISOString();
}}

function randomTargetHSV() {{
  return {{
    h: Math.random(),
    s: 0.15 + Math.random() * 0.85,
    v: 0.15 + Math.random() * 0.85
  }};
}}

function hsvToRgb(h, s, v) {{
  let r, g, b;
  let i = Math.floor(h * 6);
  let f = h * 6 - i;
  let p = v * (1 - s);
  let q = v * (1 - f * s);
  let t = v * (1 - (1 - f) * s);

  switch (i % 6) {{
    case 0: r = v; g = t; b = p; break;
    case 1: r = q; g = v; b = p; break;
    case 2: r = p; g = v; b = t; break;
    case 3: r = p; g = q; b = v; break;
    case 4: r = t; g = p; b = v; break;
    case 5: r = v; g = p; b = q; break;
  }}

  return [
    Math.round(r * 255),
    Math.round(g * 255),
    Math.round(b * 255)
  ];
}}

function hsvToXyz(h, s, v) {{
  const [r255, g255, b255] = hsvToRgb(h, s, v);
  let r = r255 / 255;
  let g = g255 / 255;
  let b = b255 / 255;

  function srgbToLinear(c) {{
    return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  }}

  r = srgbToLinear(r);
  g = srgbToLinear(g);
  b = srgbToLinear(b);

  const x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375;
  const y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750;
  const z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041;

  return [x, y, z];
}}

function xyzToLab(x, y, z) {{
  const Xn = 0.95047;
  const Yn = 1.00000;
  const Zn = 1.08883;

  function f(t) {{
    const delta = 6 / 29;
    return t > Math.pow(delta, 3)
      ? Math.cbrt(t)
      : (t / (3 * delta * delta)) + 4 / 29;
  }}

  const fx = f(x / Xn);
  const fy = f(y / Yn);
  const fz = f(z / Zn);

  const L = 116 * fy - 16;
  const a = 500 * (fx - fy);
  const b = 200 * (fy - fz);

  return [L, a, b];
}}

function hsvToLab(h, s, v) {{
  const [x, y, z] = hsvToXyz(h, s, v);
  return xyzToLab(x, y, z);
}}

function ciede2000(lab1, lab2) {{
  const [L1, a1, b1] = lab1;
  const [L2, a2, b2] = lab2;

  const kL = 1;
  const kC = 1;
  const kH = 1;

  const C1 = Math.sqrt(a1 * a1 + b1 * b1);
  const C2 = Math.sqrt(a2 * a2 + b2 * b2);
  const Cbar = (C1 + C2) / 2;

  const G = 0.5 * (
    1 - Math.sqrt(Math.pow(Cbar, 7) / (Math.pow(Cbar, 7) + Math.pow(25, 7)))
  );

  const a1p = (1 + G) * a1;
  const a2p = (1 + G) * a2;

  const C1p = Math.sqrt(a1p * a1p + b1 * b1);
  const C2p = Math.sqrt(a2p * a2p + b2 * b2);

  function hpFun(x, y) {{
    if (x === 0 && y === 0) return 0;
    let h = Math.atan2(y, x) * 180 / Math.PI;
    if (h < 0) h += 360;
    return h;
  }}

  const h1p = hpFun(a1p, b1);
  const h2p = hpFun(a2p, b2);

  const dLp = L2 - L1;
  const dCp = C2p - C1p;

  let dhp = 0;
  if (C1p * C2p === 0) {{
    dhp = 0;
  }} else if (Math.abs(h2p - h1p) <= 180) {{
    dhp = h2p - h1p;
  }} else if (h2p <= h1p) {{
    dhp = h2p - h1p + 360;
  }} else {{
    dhp = h2p - h1p - 360;
  }}

  const dHp = 2 * Math.sqrt(C1p * C2p) * Math.sin((dhp / 2) * Math.PI / 180);

  const Lbarp = (L1 + L2) / 2;
  const Cbarp = (C1p + C2p) / 2;

  let hbarp = 0;
  if (C1p * C2p === 0) {{
    hbarp = h1p + h2p;
  }} else if (Math.abs(h1p - h2p) <= 180) {{
    hbarp = (h1p + h2p) / 2;
  }} else if ((h1p + h2p) < 360) {{
    hbarp = (h1p + h2p + 360) / 2;
  }} else {{
    hbarp = (h1p + h2p - 360) / 2;
  }}

  const T =
    1
    - 0.17 * Math.cos((hbarp - 30) * Math.PI / 180)
    + 0.24 * Math.cos((2 * hbarp) * Math.PI / 180)
    + 0.32 * Math.cos((3 * hbarp + 6) * Math.PI / 180)
    - 0.20 * Math.cos((4 * hbarp - 63) * Math.PI / 180);

  const deltaTheta = 30 * Math.exp(-Math.pow((hbarp - 275) / 25, 2));
  const Rc = 2 * Math.sqrt(Math.pow(Cbarp, 7) / (Math.pow(Cbarp, 7) + Math.pow(25, 7)));

  const Sl = 1 + (0.015 * Math.pow(Lbarp - 50, 2)) / Math.sqrt(20 + Math.pow(Lbarp - 50, 2));
  const Sc = 1 + 0.045 * Cbarp;
  const Sh = 1 + 0.015 * Cbarp * T;
  const Rt = -Math.sin(2 * deltaTheta * Math.PI / 180) * Rc;

  const dE = Math.sqrt(
    Math.pow(dLp / (kL * Sl), 2) +
    Math.pow(dCp / (kC * Sc), 2) +
    Math.pow(dHp / (kH * Sh), 2) +
    Rt * (dCp / (kC * Sc)) * (dHp / (kH * Sh))
  );

  return dE;
}}

function hueDiffDegrees(h1, h2) {{
  const deg1 = h1 * 360;
  const deg2 = h2 * 360;
  let diff = Math.abs(deg1 - deg2);
  if (diff > 180) diff = 360 - diff;
  return diff;
}}

function scoreRound(target, guess) {{
  const targetLab = hsvToLab(target.h, target.s, target.v);
  const guessLab = hsvToLab(guess.h, guess.s, guess.v);

  const dE = ciede2000(targetLab, guessLab);
  const base = 10 / (1 + Math.pow(dE / 25.25, 1.55));

  const hueDiff = hueDiffDegrees(target.h, guess.h);
  const avgSatPct = ((target.s + guess.s) / 2) * 100;

  const hueAccuracy = Math.max(0, 1 - Math.pow(hueDiff / 25, 1.5));
  const recoverySatWeight = Math.min(1, avgSatPct / 30);
  const recovery = (10 - base) * hueAccuracy * recoverySatWeight * 0.25;

  const huePenaltyFactor = Math.max(0, (hueDiff - 30) / 150);
  const penaltySatWeight = Math.min(1, avgSatPct / 40);
  const penalty = base * huePenaltyFactor * penaltySatWeight * 0.15;

  const finalScore = Math.max(0, Math.min(10, base + recovery - penalty));

  return {{
    dE,
    base,
    recovery,
    penalty,
    finalScore,
    hueDiff
  }};
}}

function toHex(x) {{
  return x.toString(16).padStart(2, "0");
}}

function hsvToHex(h, s, v) {{
  const [r, g, b] = hsvToRgb(h, s, v);
  return "#" + toHex(r) + toHex(g) + toHex(b);
}}

function formatHSV(h, s, v) {{
  return `
    <div style="text-align:center;">Hue: ${{(h * 360).toFixed(0)}}°</div>
    <div style="text-align:center;">Saturation: ${{(s * 100).toFixed(0)}}%</div>
    <div style="text-align:center;">Brightness: ${{(v * 100).toFixed(0)}}%</div>
  `;
}}

function formatHSVSingleLine(h, s, v) {{
  return `H ${{(h * 360).toFixed(0)}}° • S ${{(s * 100).toFixed(0)}}% • B ${{(v * 100).toFixed(0)}}%`;
}}

function setTargetBoxColor() {{
  const hex = hsvToHex(targetHSV.h, targetHSV.s, targetHSV.v);
  document.getElementById("targetBox").style.background = hex;
}}

function updateRoundIndicators() {{
  document.getElementById("roundResultHeading").textContent = `Round ${{currentRound}} Results`;
}}

function updateReadouts() {{
  const h = parseFloat(document.getElementById("h").value);
  const s = parseFloat(document.getElementById("s").value);
  const v = parseFloat(document.getElementById("v").value);

  document.getElementById("hValue").textContent = `${{Math.round(h)}}°`;
  document.getElementById("sValue").textContent = `${{Math.round(s)}}%`;
  document.getElementById("vValue").textContent = `${{Math.round(v)}}%`;
}}

function tsvEscape(value) {{
  return String(value ?? "").replace(/\\t/g, " ").replace(/\\r?\\n/g, " ");
}}

function buildTsv(rows, columns) {{
  const lines = [];
  lines.push(columns.join("\\t"));
  for (const row of rows) {{
    lines.push(columns.map(col => tsvEscape(row[col])).join("\\t"));
  }}
  return lines.join("\\r\\n");
}}

function setDownloadLink(elementId, text, filename) {{
  const utf8Bom = "\\uFEFF";
  const blob = new Blob([utf8Bom, text], {{
    type: "text/tab-separated-values;charset=utf-8;"
  }});
  const url = URL.createObjectURL(blob);
  const link = document.getElementById(elementId);
  link.href = url;
  link.download = filename;
}}

function prepareTsvDownloads() {{
  const roundColumns = [
    "participant_id",
    "session_id",
    "session_start_timestamp",
    "round_timestamp",
    "round_number",
    "total_rounds",
    "target_h",
    "target_s",
    "target_v",
    "target_hex",
    "initial_h",
    "initial_s",
    "initial_v",
    "guess_h",
    "guess_s",
    "guess_v",
    "guess_hex",
    "delta_e_ciede2000",
    "hue_diff_deg",
    "score_base",
    "score_recovery",
    "score_penalty",
    "score_final",
    "elapsed_seconds",
    "completed_game"
  ];

  const sessionColumns = [
    "participant_id",
    "session_id",
    "session_start_timestamp",
    "session_end_timestamp",
    "total_rounds",
    "completed_rounds",
    "completed_game",
    "total_score",
    "average_score",
    "total_adjust_time_seconds",
    "mean_adjust_time_seconds"
  ];

  const roundTsv = buildTsv(roundResults, roundColumns);
  const sessionTsv = buildTsv(sessionResults, sessionColumns);

  setDownloadLink(
    "downloadRoundsBtn",
    roundTsv,
    `${{sessionId}}_round_level_results.tsv`
  );

  setDownloadLink(
    "downloadSessionBtn",
    sessionTsv,
    `${{sessionId}}_game_level_results.tsv`
  );
}}

function setSaveStatus(text) {{
  document.getElementById("saveStatus").textContent = text;
}}

async function saveResultsToGoogleSheets(gameRow, roundRows) {{
  setSaveStatus("Saving results to Google Sheets...");

  const payload = {{
    type: "batch",
    game: gameRow,
    rounds: roundRows
  }};

  try {{
    const response = await fetch(APPS_SCRIPT_URL, {{
      method: "POST",
      headers: {{
        "Content-Type": "text/plain;charset=utf-8"
      }},
      body: JSON.stringify(payload)
    }});

    const text = await response.text();
    let data = null;

    try {{
      data = JSON.parse(text);
    }} catch (err) {{
      throw new Error("Non-JSON response: " + text);
    }}

    if (!response.ok || !data.ok) {{
      throw new Error(data && data.error ? data.error : "Unknown save error");
    }}

    resultsSaved = true;
    setSaveStatus("Saved to Google Sheets.");
  }} catch (err) {{
    console.error(err);
    setSaveStatus("Could not save to Google Sheets. Files are still available for download.");
  }}
}}

function saveRoundResult() {{
  const h = parseFloat(document.getElementById("h").value) / 360;
  const s = parseFloat(document.getElementById("s").value) / 100;
  const v = parseFloat(document.getElementById("v").value) / 100;

  const guessHSV = {{ h, s, v }};
  const score = scoreRound(targetHSV, guessHSV);

  const adjustEndTime = performance.now();
  const elapsedSeconds = adjustStartTime
    ? (adjustEndTime - adjustStartTime) / 1000
    : 0;

  const targetHex = hsvToHex(targetHSV.h, targetHSV.s, targetHSV.v);
  const playerHex = hsvToHex(h, s, v);

  const row = {{
    participant_id: playerName,
    session_id: sessionId,
    session_start_timestamp: currentSessionStartTimestamp,
    round_timestamp: nowIso(),
    round_number: currentRound,
    total_rounds: TOTAL_ROUNDS,
    target_h: targetHSV.h.toFixed(6),
    target_s: targetHSV.s.toFixed(6),
    target_v: targetHSV.v.toFixed(6),
    target_hex: targetHex,
    initial_h: currentRoundInitialHSV.h.toFixed(6),
    initial_s: currentRoundInitialHSV.s.toFixed(6),
    initial_v: currentRoundInitialHSV.v.toFixed(6),
    guess_h: h.toFixed(6),
    guess_s: s.toFixed(6),
    guess_v: v.toFixed(6),
    guess_hex: playerHex,
    delta_e_ciede2000: score.dE.toFixed(6),
    hue_diff_deg: score.hueDiff.toFixed(6),
    score_base: score.base.toFixed(6),
    score_recovery: score.recovery.toFixed(6),
    score_penalty: score.penalty.toFixed(6),
    score_final: score.finalScore.toFixed(6),
    elapsed_seconds: elapsedSeconds.toFixed(6),
    completed_game: currentRound === TOTAL_ROUNDS ? "1" : "0",

    round: currentRound,
    targetHSV: {{ ...targetHSV }},
    guessHSV,
    targetHex,
    playerHex,
    elapsedSeconds,
    score
  }};

  roundResults.push(row);
  return row;
}}

function showResults() {{
  const roundData = saveRoundResult();

  document.getElementById("playActionArea").style.display = "none";
  document.getElementById("targetColorBox").style.background = roundData.targetHex;
  document.getElementById("playerColorBox").style.background = roundData.playerHex;

  document.getElementById("targetInfo").innerHTML =
    formatHSV(roundData.targetHSV.h, roundData.targetHSV.s, roundData.targetHSV.v);

  document.getElementById("playerInfo").innerHTML =
    formatHSV(roundData.guessHSV.h, roundData.guessHSV.s, roundData.guessHSV.v);

  document.getElementById("timeSpentDisplay").textContent =
    `Time spent adjusting: ${{roundData.elapsedSeconds.toFixed(2)}}s`;

  document.getElementById("scoreValue").textContent =
    `${{roundData.score.finalScore.toFixed(2)}}`;

  document.getElementById("playerColorSection").style.display = "none";
  document.getElementById("controlsSection").style.display = "none";
  document.getElementById("results").style.display = "block";

  const btn = document.getElementById("resultsActionBtn");
  btn.textContent = currentRound < TOTAL_ROUNDS ? "Next round" : "See final results";
  btn.onclick = currentRound < TOTAL_ROUNDS ? startNextRound : showFinalSummary;
  document.getElementById("resultsActionArea").style.display = "flex";
}}

function startNextRound() {{
  currentRound += 1;
  targetHSV = randomTargetHSV();
  setTargetBoxColor();
  adjustStartTime = null;
  currentRoundInitialHSV = null;
  updateRoundIndicators();

  document.getElementById("countdownPhase").style.display = "block";
  document.getElementById("countdownPhase").textContent = "3";

  document.getElementById("targetPhase").style.display = "none";
  document.getElementById("playPhase").style.display = "none";
  document.getElementById("results").style.display = "none";
  document.getElementById("resultsActionArea").style.display = "none";
  document.getElementById("finalSummary").style.display = "none";
  document.getElementById("playActionArea").style.display = "none";

  document.getElementById("playerColorSection").style.display = "flex";
  document.getElementById("controlsSection").style.display = "flex";

  startCountdown();
}}

async function showFinalSummary() {{
  document.getElementById("results").style.display = "none";
  document.getElementById("resultsActionArea").style.display = "none";
  document.getElementById("playActionArea").style.display = "none";
  document.getElementById("playerColorSection").style.display = "none";
  document.getElementById("controlsSection").style.display = "none";

  const summaryRows = document.getElementById("summaryRows");
  summaryRows.innerHTML = "";

  const totalScore = roundResults.reduce((sum, r) => sum + parseFloat(r.score_final), 0);
  const avgScore = roundResults.length ? totalScore / roundResults.length : 0;
  const totalTime = roundResults.reduce((sum, r) => sum + parseFloat(r.elapsed_seconds), 0);
  const meanTime = roundResults.length ? totalTime / roundResults.length : 0;
  const sessionEndTimestamp = nowIso();

  const completedGameValue = roundResults.length === TOTAL_ROUNDS ? "1" : "0";

  const sessionRow = {{
    participant_id: playerName,
    session_id: sessionId,
    session_start_timestamp: currentSessionStartTimestamp,
    session_end_timestamp: sessionEndTimestamp,
    total_rounds: TOTAL_ROUNDS,
    completed_rounds: roundResults.length,
    completed_game: completedGameValue,
    total_score: totalScore.toFixed(6),
    average_score: avgScore.toFixed(6),
    total_adjust_time_seconds: totalTime.toFixed(6),
    mean_adjust_time_seconds: meanTime.toFixed(6)
  }};

  sessionResults = [sessionRow];
  roundResults = roundResults.map(r => ({{
    ...r,
    completed_game: completedGameValue
  }}));

  document.getElementById("playerNameFinal").textContent = `Player: ${{playerName}}`;
  document.getElementById("finalStats").textContent =
    `Total: ${{totalScore.toFixed(2)}} • Average: ${{avgScore.toFixed(2)}} • Total adjust time: ${{totalTime.toFixed(2)}}s`;

  const header = document.createElement("div");
  header.className = "summary-card";
  header.innerHTML = `
    <div class="summary-grid">
      <div class="summary-head">Round</div>
      <div class="summary-head">Original</div>
      <div class="summary-head">Yours</div>
      <div class="summary-head">Score</div>
      <div class="summary-head">Time</div>
    </div>
  `;
  summaryRows.appendChild(header);

  roundResults.forEach((r) => {{
    const row = document.createElement("div");
    row.className = "summary-card";
    row.innerHTML = `
      <div class="summary-grid">
        <div class="summary-cell" style="font-weight:800;">${{r.round}}</div>

        <div class="summary-cell">
          <div class="mini-swatch-wrap">
            <div class="mini-swatch-block">
              <div class="mini-swatch" style="background:${{r.targetHex}};"></div>
              <div class="compact-color-line">
                ${{formatHSVSingleLine(r.targetHSV.h, r.targetHSV.s, r.targetHSV.v)}}
              </div>
            </div>
          </div>
        </div>

        <div class="summary-cell">
          <div class="mini-swatch-wrap">
            <div class="mini-swatch-block">
              <div class="mini-swatch" style="background:${{r.playerHex}};"></div>
              <div class="compact-color-line">
                ${{formatHSVSingleLine(r.guessHSV.h, r.guessHSV.s, r.guessHSV.v)}}
              </div>
            </div>
          </div>
        </div>

        <div class="summary-cell" style="font-weight:700;">${{parseFloat(r.score_final).toFixed(2)}}</div>
        <div class="summary-cell">${{parseFloat(r.elapsed_seconds).toFixed(2)}}s</div>
      </div>
    `;
    summaryRows.appendChild(row);
  }});

  prepareTsvDownloads();
  document.getElementById("finalSummary").style.display = "block";

  if (!resultsSaved) {{
    await saveResultsToGoogleSheets(sessionRow, roundResults);
  }}
}}

function resetGame() {{
  if (countdownInterval) clearInterval(countdownInterval);
  if (revealTimeout) clearTimeout(revealTimeout);

  currentRound = 1;
  roundResults = [];
  sessionResults = [];
  targetHSV = randomTargetHSV();
  setTargetBoxColor();
  adjustStartTime = null;
  currentRoundInitialHSV = null;
  sessionId = generateSessionId();
  currentSessionStartTimestamp = "";
  resultsSaved = false;

  document.getElementById("startScreen").style.display = "flex";
  document.getElementById("gameContainer").style.display = "none";
  document.getElementById("playerNameInput").value = playerName;
  document.getElementById("startValidation").textContent = "";
  document.getElementById("countdownPhase").textContent = "3";
  document.getElementById("targetPhase").style.display = "none";
  document.getElementById("playPhase").style.display = "none";
  document.getElementById("results").style.display = "none";
  document.getElementById("resultsActionArea").style.display = "none";
  document.getElementById("finalSummary").style.display = "none";
  document.getElementById("playActionArea").style.display = "none";
  document.getElementById("saveStatus").textContent = "";

  updateRoundIndicators();
}}

function beginGame() {{
  const input = document.getElementById("playerNameInput");
  const validation = document.getElementById("startValidation");
  const trimmed = input.value.trim();

  if (!trimmed) {{
    validation.textContent = "Please enter your name to start.";
    input.focus();
    return;
  }}

  playerName = trimmed;
  validation.textContent = "";

  currentRound = 1;
  roundResults = [];
  sessionResults = [];
  targetHSV = randomTargetHSV();
  setTargetBoxColor();
  adjustStartTime = null;
  currentRoundInitialHSV = null;
  sessionId = generateSessionId();
  currentSessionStartTimestamp = nowIso();
  resultsSaved = false;
  updateRoundIndicators();

  document.getElementById("startScreen").style.display = "none";
  document.getElementById("gameContainer").style.display = "flex";

  document.getElementById("countdownPhase").style.display = "block";
  document.getElementById("countdownPhase").textContent = "3";
  document.getElementById("targetPhase").style.display = "none";
  document.getElementById("playPhase").style.display = "none";
  document.getElementById("results").style.display = "none";
  document.getElementById("resultsActionArea").style.display = "none";
  document.getElementById("finalSummary").style.display = "none";
  document.getElementById("playActionArea").style.display = "none";
  document.getElementById("saveStatus").textContent = "";

  startCountdown();
}}

function setRandomColor() {{
  const h = Math.random() * 360;
  const s = 15 + Math.random() * 85;
  const v = 15 + Math.random() * 85;

  const hRounded = Math.round(h);
  const sRounded = Math.round(s);
  const vRounded = Math.round(v);

  document.getElementById("h").value = hRounded;
  document.getElementById("s").value = sRounded;
  document.getElementById("v").value = vRounded;

  currentRoundInitialHSV = {{
    h: hRounded / 360,
    s: sRounded / 100,
    v: vRounded / 100
  }};

  updateReadouts();
}}

function updateColor() {{
  const h = parseFloat(document.getElementById("h").value) / 360;
  const s = parseFloat(document.getElementById("s").value) / 100;
  const v = parseFloat(document.getElementById("v").value) / 100;

  const hex = hsvToHex(h, s, v);
  document.getElementById("preview").style.background = hex;
}}

function updateSliderBackgrounds() {{
  const h = parseFloat(document.getElementById("h").value) / 360;
  const v = parseFloat(document.getElementById("v").value) / 100;

  const [r, g, b] = hsvToRgb(h, 1, v);
  const fullColor = `rgb(${{r}}, ${{g}}, ${{b}})`;

  const greyValue = Math.round(v * 255);
  const grey = `rgb(${{greyValue}}, ${{greyValue}}, ${{greyValue}})`;

  document.getElementById("s").style.background =
    `linear-gradient(to right, ${{grey}}, ${{fullColor}})`;

  document.getElementById("v").style.background =
    `linear-gradient(to right, black, ${{fullColor}})`;
}}

function handleSliderInput() {{
  updateReadouts();
  updateColor();
  updateSliderBackgrounds();
}}

document.getElementById("h").addEventListener("input", handleSliderInput);
document.getElementById("s").addEventListener("input", handleSliderInput);
document.getElementById("v").addEventListener("input", handleSliderInput);
document.getElementById("restartBtn").addEventListener("click", resetGame);
document.getElementById("startGameBtn").addEventListener("click", beginGame);
document.getElementById("playActionBtn").addEventListener("click", showResults);
document.getElementById("playerNameInput").addEventListener("keydown", (e) => {{
  if (e.key === "Enter") beginGame();
}});
document.getElementById("playerNameInput").addEventListener("input", () => {{
  document.getElementById("startValidation").textContent = "";
}});

function startCountdown() {{
  let count = 3;
  const el = document.getElementById("countdownPhase");
  el.textContent = "3";
  el.style.display = "block";

  countdownInterval = setInterval(() => {{
    count--;
    if (count > 0) {{
      el.textContent = count;
    }} else {{
      clearInterval(countdownInterval);
      countdownInterval = null;

      el.style.display = "none";

      const targetPhase = document.getElementById("targetPhase");
      targetPhase.style.display = "block";
      setTargetBoxColor();

      revealTimeout = setTimeout(() => {{
        revealTimeout = null;

        targetPhase.style.display = "none";
        document.getElementById("playPhase").style.display = "flex";
        document.getElementById("playerColorSection").style.display = "flex";
        document.getElementById("controlsSection").style.display = "flex";
        document.getElementById("results").style.display = "none";
        document.getElementById("resultsActionArea").style.display = "none";
        document.getElementById("finalSummary").style.display = "none";

        document.getElementById("playActionArea").style.display = "flex";

        setRandomColor();
        updateColor();
        updateSliderBackgrounds();
        adjustStartTime = performance.now();
      }}, 5000);
    }}
  }}, 1000);
}}

sessionId = generateSessionId();
updateRoundIndicators();
setTargetBoxColor();
</script>
"""

left_spacer, main_col, right_spacer = st.columns([1.6, 6, 1.0])

with main_col:
    components.html(html, height=1820)