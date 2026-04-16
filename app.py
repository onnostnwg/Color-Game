import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Color Memory Game", layout="wide")

st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 0rem;
}
</style>
""", unsafe_allow_html=True)

APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxmuZRNR9qR1sFFPe7TMeRrAJo6sBkVSRkmftl-wq5hDMSVOmFbNLzBK_Sfj2QnW6a5/exec"

html = f"""
<style>

html,
body {{
  margin: 0;
  padding: 0;
}}

.timer-overlay {{
  position: absolute;
  top: 12px;
  right: 12px;
  z-index: 20;
  background: rgba(20,20,20,0.58);
  border: 1px solid rgba(255,255,255,0.14);
  border-radius: 10px;
  padding: 8px 10px;
  color: white;
  font-family: monospace;
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.5px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.28);
  display: none;
  pointer-events: none;
}}

.round-overlay {{
  position: absolute;
  top: 12px;
  left: 12px;
  z-index: 20;
  background: rgba(20,20,20,0.58);
  border: 1px solid rgba(255,255,255,0.14);
  border-radius: 10px;
  padding: 8px 10px;
  color: white;
  font-family: monospace;
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.5px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.28);
  pointer-events: none;
}}

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
  border-radius: 18px;
  padding: 16px;
  box-sizing: border-box;
  min-width: 0;
}}

.round-card-top {{
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 6px;
  margin-bottom: 12px;
}}

.round-card-title {{
  font-size: 16px;
  font-weight: 800;
  line-height: 1.2;
  width: 100%;
  text-align: center;
}}

.round-card-score {{
  font-size: 16px;
  font-weight: 800;
  white-space: nowrap;
  width: 100%;
  text-align: center;
}}

.round-card-subtitle {{
  font-size: 12px;
  opacity: 0.82;
  line-height: 1.25;
  text-align: center;
}}

.combined-color-panel {{
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.12);
  background: rgba(255,255,255,0.03);
  margin-top: 10px;
}}

.combined-color-half {{
  height: 88px;
  width: 100%;
  position: relative;
}}

.combined-color-half-label {{
  position: absolute;
  left: 10px;
  bottom: 10px;
  font-size: 11px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.4px;
  color: white;
  background: rgba(0,0,0,0.34);
  padding: 4px 8px;
  border-radius: 8px;
}}

.final-meta-row {{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 32px;
  margin-top: 14px;
  margin-bottom: 12px;
  font-size: 15px;
  font-weight: 600;
  opacity: 0.95;
  flex-wrap: wrap;
}}

.final-stats-line {{
  margin-top: 8px;
}}

.current-rank-display {{
  margin-top: 8px;
  margin-bottom: 18px;
  font-size: 16px;
  font-weight: 800;
  text-align: center;
  opacity: 0.95;
}}

.summary-header-card {{
  grid-column: 1 / -1;
  width: 100%;
  background: #242424;
  border: 1px solid #444;
  border-radius: 18px;
  padding: 14px 18px;
  box-sizing: border-box;
  font-size: 14px;
  font-weight: 700;
  opacity: 0.92;
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

.leaderboard-row {{
  display: grid;
  grid-template-columns: 92px 1fr 140px;
  align-items: center;
  gap: 14px;
  padding: 14px 16px;
  border-radius: 14px;
  background: #242424;
  border: 1px solid #444;
}}

.leaderboard-rank {{
  font-size: 22px;
  font-weight: 800;
  text-align: center;
}}

.leaderboard-name {{
  font-size: 16px;
  font-weight: 700;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}}

.leaderboard-score {{
  font-size: 18px;
  font-weight: 800;
  text-align: right;
}}

.leaderboard-section {{
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.leaderboard-mode-title {{
  font-size: 18px;
  font-weight: 800;
  margin-top: 8px;
}}

.leaderboard-empty {{
  text-align: center;
  opacity: 0.8;
  padding: 24px 12px;
  border: 1px dashed #555;
  border-radius: 14px;
}}

#targetBox,
#preview {{
  width: min(300px, 82vw) !important;
  height: min(300px, 82vw) !important;
}}

#playerColorSection {{
  width: min(300px, 82vw) !important;
}}

#controlsSection {{
  width: min(400px, 88vw) !important;
}}

#results {{
  width: min(500px, 92vw) !important;
}}

#finalSummary {{
  width: min(980px, 94vw) !important;
}}

#leaderboardScreen {{
  width: min(760px, 94vw) !important;
}}

#resultsDetails > div {{
  width: min(456px, 86vw) !important;
}}

@media (max-width: 700px) {{
  .start-screen {{
    margin-top: 56px;
    gap: 16px;
  }}

  .start-title {{
    font-size: 32px;
  }}

  #countdownPhase {{
    font-size: 96px !important;
    margin-top: 80px !important;
  }}

  #playPhase {{
    gap: 22px !important;
    margin-top: 20px !important;
  }}

  #targetPhase {{
    margin-top: 20px !important;
  }}

  #scoreDisplay {{
    font-size: 52px !important;
  }}

  #colorComparison {{
    gap: 16px !important;
  }}

  #resultsDetails > div {{
    flex-direction: column !important;
    align-items: center !important;
    gap: 16px !important;
  }}

  #summaryRows {{
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }}

  .combined-color-half {{
    height: 72px;
  }}
}}

@media (max-width: 520px) {{
  .primary-btn {{
    padding: 11px 14px;
    font-size: 15px;
  }}

  .round-overlay,
  .timer-overlay {{
    top: 8px;
    padding: 6px 8px;
    font-size: 15px;
  }}

  .round-overlay {{
    left: 8px;
  }}

  .timer-overlay {{
    right: 8px;
  }}

  #summaryRows {{
    grid-template-columns: 1fr !important;
  }}

  .summary-card {{
    padding: 14px;
  }}

  .leaderboard-row {{
    grid-template-columns: 54px minmax(0, 1fr) 76px;
    gap: 8px;
    padding: 12px 10px;
  }}

  .leaderboard-rank {{
    font-size: 18px;
  }}

  .leaderboard-name {{
    font-size: 14px;
  }}

  .leaderboard-score {{
    font-size: 15px;
  }}

  .final-meta-row {{
    gap: 10px;
    flex-direction: column;
  }}
}}

</style>

<div id="appRoot" style="font-family:sans-serif; display:flex; flex-direction:column; align-items:center; gap:24px; color:white;">

  <div id="startScreen" class="start-screen">
  <div class="start-title">Color Memory Game</div>
  <div class="start-subtitle">Enter your name to begin</div>

  <input id="playerNameInput" class="name-input" type="text" maxlength="40" placeholder="Your name" />

<div style="margin-top:10px; text-align:center;">
  <div style="font-size:14px; margin-bottom:6px; opacity:0.9;">
    Choose game mode
  </div>
  <div style="display:flex; gap:10px; justify-content:center;">
    <button type="button" id="modeEasy" class="primary-btn" style="background:#ffffff; color:black;">Easy</button>
    <button type="button" id="modeHard" class="primary-btn" style="background:#333; color:white;">Hard</button>
  </div>
</div>

  <button id="startGameBtn" class="primary-btn">Start Game</button>
  <div id="startValidation" class="validation-text"></div>
</div>

  <div id="gameContainer" style="display:none; width:100%; flex-direction:column; align-items:center; gap:30px;">
    <div id="countdownPhase" style="
      font-size:140px;
      font-weight:bold;
      margin-top:120px;
    ">3</div>

    <div id="targetPhase" style="display:none; text-align:center; margin-top:30px; width:100%;">
      <div style="position:relative; display:inline-block;">
        <div id="targetBox" style="width:300px; height:300px; border-radius:16px; border:2px solid #555;"></div>
        <div id="targetRoundIndicator" class="round-overlay">1/5</div>
        <div id="targetTimer" class="timer-overlay">5.000</div>
      </div>
    </div>

    <div id="playPhase" style="display:none; flex-direction:column; align-items:center; gap:30px; margin-top:30px;">

      <div id="playerColorSection" style="position:relative; display:flex; justify-content:center; width:300px;">
        <div style="text-align:center;">
          <div id="preview" style="
            width:300px;
            height:300px;
            background:#408080;
            border-radius:16px;
            border:2px solid #555;">
          </div>
          <div id="playRoundIndicator" class="round-overlay">1/5</div>
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
  margin-bottom:10px;
  letter-spacing:-1px;
">
  Score: <span id="scoreValue">0.00</span>
</div>

<div id="roundCommentDisplay" style="
  font-size:20px;
  font-weight:700;
  text-align:center;
  margin-bottom:22px;
  opacity:0.95;
">
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
  <div class="final-meta-row">
    <div id="playerNameFinal"></div>
    <div id="gameModeFinal"></div>
  </div>
  <div class="phase-subtitle final-stats-line" id="finalStats">Total: 0.00 • Average: 0.00</div>

  <div id="summaryRows" style="
    display:grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap:14px;
    margin-top:24px;
    width:100%;
  "></div>

  <div style="display:flex; justify-content:center; margin-top:24px; gap:14px; flex-wrap:wrap;">
    <button id="restartBtn" class="primary-btn">
      Play Again
    </button>
    <button id="openLeaderboardBtn" class="primary-btn">
      See Leaderboard
    </button>
  </div>
</div>

<div id="leaderboardScreen" style="
  display:none;
  width:760px;
  margin-top:20px;
  padding:24px 20px 20px 20px;
  border-radius:16px;
  background:#1e1e1e;
  border:1px solid #444;
  color:white;
  box-sizing:border-box;
">
  <div class="phase-title">Leaderboard</div>
  <div class="phase-subtitle" style="margin-bottom:22px;">
    Top 5 scores by game mode
  </div>
  <div id="leaderboardRankDisplay" class="current-rank-display"></div>

  <div id="leaderboardTable" style="
    display:flex;
    flex-direction:column;
    gap:10px;
    width:100%;
  "></div>

  <div style="display:flex; justify-content:center; gap:14px; margin-top:24px; flex-wrap:wrap;">
    <button id="backToFinalBtn" class="primary-btn">Back to final results</button>
    <button id="restartFromLeaderboardBtn" class="primary-btn">Play again</button>
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
let savedRoundIds = new Set();
let targetTimerInterval = null;
let targetRevealEndTime = null;
let gameMode = "easy";
let lastCompletedGameRow = null;
let leaderboardDataCache = null;
let leaderboardFetchPromise = null;

let resizeFrameTimeout = null;

function resizeStreamlitFrame() {{
  if (resizeFrameTimeout) clearTimeout(resizeFrameTimeout);

  resizeFrameTimeout = setTimeout(() => {{
    const root = document.getElementById("appRoot");
    const rootHeight = root ? root.getBoundingClientRect().height : document.body.scrollHeight;
    const height = Math.ceil(rootHeight + 80);

    if (window.frameElement) {{
      window.frameElement.style.height = `${{height}}px`;
    }}

    window.parent.postMessage({{
      isStreamlitMessage: true,
      type: "streamlit:setFrameHeight",
      height
    }}, "*");
  }}, 40);
}}

window.addEventListener("load", resizeStreamlitFrame);
window.addEventListener("resize", resizeStreamlitFrame);

if ("ResizeObserver" in window) {{
  const frameResizeObserver = new ResizeObserver(resizeStreamlitFrame);
  frameResizeObserver.observe(document.body);
}}

const frameMutationObserver = new MutationObserver(resizeStreamlitFrame);
frameMutationObserver.observe(document.body, {{
  attributes: true,
  childList: true,
  subtree: true
}});

const GAME_MODES = {{
  easy: {{
    revealMs: 5000,
    minHueDistance: 40
  }},
  hard: {{
    revealMs: 2500,
    minHueDistance: 90
  }}
}};

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

function roundComment(score) {{
  if (score >= 9) return "Dayum, u good!";
  if (score >= 7) return "Ok ok, not bad.";
  if (score >= 5) return "Oh well.";
  if (score >= 3) return "See a doctor.";
  return "U suck :(";
}}

function setTargetBoxColor() {{
  const hex = hsvToHex(targetHSV.h, targetHSV.s, targetHSV.v);
  document.getElementById("targetBox").style.background = hex;
}}

function updateRoundIndicators() {{
  const roundText = `${{currentRound}}/${{TOTAL_ROUNDS}}`;
  document.getElementById("roundResultHeading").textContent = `Round ${{currentRound}} Results`;
  document.getElementById("targetRoundIndicator").textContent = roundText;
  document.getElementById("playRoundIndicator").textContent = roundText;
}}

function updateReadouts() {{
  const h = parseFloat(document.getElementById("h").value);
  const s = parseFloat(document.getElementById("s").value);
  const v = parseFloat(document.getElementById("v").value);

  document.getElementById("hValue").textContent = `${{Math.round(h)}}°`;
  document.getElementById("sValue").textContent = `${{Math.round(s)}}%`;
  document.getElementById("vValue").textContent = `${{Math.round(v)}}%`;
}}

function setSaveStatus(text) {{
  const el = document.getElementById("saveStatus");
  if (el) {{
    el.textContent = text;
  }}
}}

async function postJsonPayload(payload) {{
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

  return data;
}}

async function saveRoundToGoogleSheets(roundRow) {{
  if (!roundRow || !roundRow.round_id) return;
  if (savedRoundIds.has(roundRow.round_id)) return;

  try {{
    await postJsonPayload({{
      type: "round",
      round: roundRow
    }});

    savedRoundIds.add(roundRow.round_id);
    console.log(`Round ${{roundRow.round_number}} saved.`);
  }} catch (err) {{
    console.error("Round save failed:", err);
  }}
}}

async function saveSessionToGoogleSheets(gameRow) {{
  setSaveStatus("Saving final game summary...");

  try {{
    await postJsonPayload({{
      type: "game",
      game: gameRow
    }});

    resultsSaved = true;
    setSaveStatus("Final game summary saved.");
  }} catch (err) {{
    console.error(err);
    setSaveStatus("Could not save final summary. Please try again later.");
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
  const roundId = `${{sessionId}}_R${{currentRound}}`;

    const row = {{
    participant_id: playerName,
    session_id: sessionId,
    round_id: roundId,
    session_start_timestamp: currentSessionStartTimestamp,
    round_timestamp: nowIso(),
    game_mode: gameMode,
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

  saveRoundToGoogleSheets(roundData).catch((err) => {{
    console.error("Round save failed:", err);
  }});

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

    document.getElementById("roundCommentDisplay").textContent =
    roundComment(roundData.score.finalScore);

  document.getElementById("playerColorSection").style.display = "none";
  document.getElementById("controlsSection").style.display = "none";
  document.getElementById("results").style.display = "block";

  const btn = document.getElementById("resultsActionBtn");
  btn.textContent = currentRound < TOTAL_ROUNDS ? "Next round" : "See final results";
  btn.onclick = currentRound < TOTAL_ROUNDS ? startNextRound : showFinalSummary;
  document.getElementById("resultsActionArea").style.display = "flex";
  resizeStreamlitFrame();
}}

function startNextRound() {{
  currentRound += 1;
  targetHSV = randomTargetHSV();
  setTargetBoxColor();
  adjustStartTime = null;
  currentRoundInitialHSV = null;
  stopTargetTimer();
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
  document.getElementById("leaderboardScreen").style.display = "none";

  startCountdown();
  resizeStreamlitFrame();
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
    game_mode: gameMode,
    total_rounds: TOTAL_ROUNDS,
    completed_rounds: roundResults.length,
    completed_game: completedGameValue,
    total_score: totalScore.toFixed(6),
    average_score: avgScore.toFixed(6),
    total_adjust_time_seconds: totalTime.toFixed(6),
    mean_adjust_time_seconds: meanTime.toFixed(6)
  }};

  sessionResults = [sessionRow];
  lastCompletedGameRow = sessionRow;
  roundResults = roundResults.map(r => ({{
    ...r,
    completed_game: completedGameValue
  }}));

  document.getElementById("playerNameFinal").textContent = `Player: ${{playerName}}`;
  document.getElementById("gameModeFinal").textContent =
    `Mode: ${{gameMode.charAt(0).toUpperCase() + gameMode.slice(1)}}`;
  document.getElementById("finalStats").textContent =
  `Total: ${{totalScore.toFixed(2)}} • Average: ${{avgScore.toFixed(2)}}`;

      roundResults.forEach((r) => {{
    const row = document.createElement("div");
    row.className = "summary-card";

    const scoreText = parseFloat(r.score_final).toFixed(2);
    const comment = roundComment(parseFloat(r.score_final));

    row.innerHTML = `
      <div class="round-card-top">
        <div class="round-card-title">Round ${{r.round}}</div>
        <div class="round-card-score">${{scoreText}} / 10</div>
        <div class="round-card-subtitle">${{comment}}</div>
      </div>

      <div class="combined-color-panel">
        <div class="combined-color-half" style="background:${{r.targetHex}};">
          <div class="combined-color-half-label">Original</div>
        </div>
        <div class="combined-color-half" style="background:${{r.playerHex}};">
          <div class="combined-color-half-label">Yours</div>
        </div>
      </div>
    `;
    summaryRows.appendChild(row);
  }});

  document.getElementById("finalSummary").style.display = "block";

  if (!resultsSaved) {{
    await saveSessionToGoogleSheets(sessionRow);
  }}

  loadLeaderboardData(true).catch((err) => {{
    console.error("Leaderboard prefetch failed:", err);
  }});
  resizeStreamlitFrame();
}}

function resetGame() {{
  if (countdownInterval) clearInterval(countdownInterval);
  if (revealTimeout) clearTimeout(revealTimeout);
  stopTargetTimer(); 

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
  savedRoundIds = new Set();
  lastCompletedGameRow = null;
  leaderboardDataCache = null;
  leaderboardFetchPromise = null;

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
  document.getElementById("gameModeFinal").textContent = "";
  document.getElementById("leaderboardRankDisplay").textContent = "";
  document.getElementById("leaderboardScreen").style.display = "none";

  updateRoundIndicators();
  resizeStreamlitFrame();
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
  savedRoundIds = new Set();
  lastCompletedGameRow = null;
  leaderboardDataCache = null;
  leaderboardFetchPromise = null;
  stopTargetTimer();
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
  document.getElementById("leaderboardScreen").style.display = "none";

  startCountdown();
  resizeStreamlitFrame();
}}

function setRandomColor() {{
  const MIN_HUE_DISTANCE = GAME_MODES[gameMode].minHueDistance;

  let h, hNorm;
  const targetDeg = targetHSV.h * 360;

  do {{
    h = Math.random() * 360;
    let diff = Math.abs(h - targetDeg);
    if (diff > 180) diff = 360 - diff;
    
    if (diff >= MIN_HUE_DISTANCE) break;
  }} while (true);

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
document.getElementById("openLeaderboardBtn").addEventListener("click", showLeaderboard);
document.getElementById("backToFinalBtn").addEventListener("click", backToFinalResults);
document.getElementById("restartFromLeaderboardBtn").addEventListener("click", resetGame);

// 👇 ADD THIS BELOW

document.getElementById("modeEasy").addEventListener("click", () => {{
  gameMode = "easy";
  document.getElementById("modeEasy").style.background = "#ffffff";
  document.getElementById("modeEasy").style.color = "black";
  document.getElementById("modeHard").style.background = "#333";
  document.getElementById("modeHard").style.color = "white";
}});

document.getElementById("modeHard").addEventListener("click", () => {{
  gameMode = "hard";
  document.getElementById("modeHard").style.background = "#ffffff";
  document.getElementById("modeHard").style.color = "black";
  document.getElementById("modeEasy").style.background = "#333";
  document.getElementById("modeEasy").style.color = "white";
}});

function stopTargetTimer() {{
  if (targetTimerInterval) {{
    clearInterval(targetTimerInterval);
    targetTimerInterval = null;
  }}

  const timerEl = document.getElementById("targetTimer");
  if (timerEl) {{
    timerEl.style.display = "none";
  }}
}}

function startTargetTimer(durationMs) {{
  stopTargetTimer();

  const timerEl = document.getElementById("targetTimer");
  if (!timerEl) return;

  targetRevealEndTime = performance.now() + durationMs;
  timerEl.style.display = "block";
  resizeStreamlitFrame();

  function renderTimer() {{
    const remainingMs = Math.max(0, targetRevealEndTime - performance.now());
    timerEl.textContent = (remainingMs / 1000).toFixed(3);

    if (remainingMs <= 0) {{
      stopTargetTimer();
    }}
  }}

  renderTimer();
  targetTimerInterval = setInterval(renderTimer, 16);
}}

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
      resizeStreamlitFrame();
      setTimeout(resizeStreamlitFrame, 120);

      const revealMs = GAME_MODES[gameMode].revealMs;

      startTargetTimer(revealMs);

      revealTimeout = setTimeout(() => {{
        revealTimeout = null;
        stopTargetTimer();

        // hide target
        targetPhase.style.display = "none";
        resizeStreamlitFrame();

        // delay before sliders
        setTimeout(() => {{
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
          resizeStreamlitFrame();
        }}, 500);

      }}, revealMs);
    }}
  }}, 1000);
}}

sessionId = generateSessionId();
updateRoundIndicators();
setTargetBoxColor();
resizeStreamlitFrame();

async function fetchLeaderboard() {{
  const params = new URLSearchParams();
  params.set("type", "leaderboard");

  if (lastCompletedGameRow) {{
    params.set("session_id", lastCompletedGameRow.session_id || "");
    params.set("game_mode", lastCompletedGameRow.game_mode || "");
    params.set("total_score", lastCompletedGameRow.total_score || "");
  }}

  const response = await fetch(`${{APPS_SCRIPT_URL}}?${{params.toString()}}`);
  const text = await response.text();

  let data = null;
  try {{
    data = JSON.parse(text);
  }} catch (err) {{
    throw new Error("Invalid leaderboard response: " + text);
  }}

  if (!response.ok || !data.ok) {{
    throw new Error(data && data.error ? data.error : "Could not load leaderboard");
  }}

  return data;
}}

async function loadLeaderboardData(forceRefresh = false) {{
  if (!forceRefresh && leaderboardDataCache) {{
    return leaderboardDataCache;
  }}

  if (!forceRefresh && leaderboardFetchPromise) {{
    return leaderboardFetchPromise;
  }}

  leaderboardFetchPromise = fetchLeaderboard()
    .then((data) => {{
      leaderboardDataCache = data;
      leaderboardFetchPromise = null;
      return data;
    }})
    .catch((err) => {{
      leaderboardFetchPromise = null;
      throw err;
    }});

  return leaderboardFetchPromise;
}}

function getRankLabel(index) {{
  const medals = ["&#129351;", "&#129352;", "&#129353;"];
  return medals[index] || `#${{index + 1}}`;
}}

function getRankedModeRows(rows, modeKey) {{
  return rows
    .filter((row) => String(row.game_mode || "").trim().toLowerCase() === modeKey)
    .sort((a, b) => parseFloat(b.total_score || 0) - parseFloat(a.total_score || 0));
}}

function getRowsWithCurrentGame(rows, gameRow) {{
  const currentSessionId = String(gameRow.session_id || "");
  const otherRows = rows.filter((row) => String(row.session_id || "") !== currentSessionId);
  return [...otherRows, gameRow];
}}

function updateLeaderboardRank(data) {{
  const el = document.getElementById("leaderboardRankDisplay");
  if (!el) return;

  if (!lastCompletedGameRow) {{
    el.textContent = "";
    return;
  }}

  if (data.currentRank && data.currentModeTotalGames) {{
    const modeKey = String(data.currentMode || lastCompletedGameRow.game_mode || "").trim().toLowerCase();
    el.textContent =
      `You came in #${{data.currentRank}} out of ${{data.currentModeTotalGames}} games played so far in ${{modeKey}} mode!`;
    return;
  }}

  const fallbackRows = Array.isArray(data.rows) ? data.rows : [];
  if (!fallbackRows.length) {{
    el.textContent = "Rank unavailable right now.";
    return;
  }}

  const modeKey = String(lastCompletedGameRow.game_mode || "").trim().toLowerCase();
  const rankedRows = getRankedModeRows(getRowsWithCurrentGame(fallbackRows, lastCompletedGameRow), modeKey);
  const rankIndex = rankedRows.findIndex((row) =>
    String(row.session_id || "") === String(lastCompletedGameRow.session_id || "")
  );

  if (rankIndex === -1) {{
    el.textContent = "Rank unavailable right now.";
    return;
  }}

  el.textContent =
    `You came in #${{rankIndex + 1}} out of ${{rankedRows.length}} games played so far in ${{modeKey}} mode!`;
}}

function getTopLeaderboardRows(rows, modeKey) {{
  return getRankedModeRows(rows, modeKey).slice(0, 5);
}}

function escapeHtml(value) {{
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}}

function renderLeaderboard(data) {{
  const table = document.getElementById("leaderboardTable");
  table.innerHTML = "";

  const fallbackRows = Array.isArray(data.rows) ? data.rows : [];
  const easyRows = Array.isArray(data.easyTop5)
    ? data.easyTop5
    : getTopLeaderboardRows(fallbackRows, "easy");
  const hardRows = Array.isArray(data.hardTop5)
    ? data.hardTop5
    : getTopLeaderboardRows(fallbackRows, "hard");

  if (!easyRows.length && !hardRows.length) {{
    table.innerHTML = `<div class="leaderboard-empty">No leaderboard data yet.</div>`;
    return;
  }}

  const modes = [
    {{ key: "easy", label: "Easy mode", rows: easyRows }},
    {{ key: "hard", label: "Hard mode", rows: hardRows }}
  ];

  modes.forEach((mode) => {{
    const section = document.createElement("div");
    section.className = "leaderboard-section";

    const title = document.createElement("div");
    title.className = "leaderboard-mode-title";
    title.textContent = mode.label;
    section.appendChild(title);

    const modeRows = mode.rows;

    if (!modeRows.length) {{
      const empty = document.createElement("div");
      empty.className = "leaderboard-empty";
      empty.textContent = `No ${{mode.key}} scores yet.`;
      section.appendChild(empty);
      table.appendChild(section);
      return;
    }}

    modeRows.forEach((row, index) => {{
      const item = document.createElement("div");
      item.className = "leaderboard-row";

      const name = row.participant_id || "Anonymous";
      const score = parseFloat(row.total_score || 0).toFixed(2);
      const rankLabel = getRankLabel(index);

      item.innerHTML = `
        <div class="leaderboard-rank">${{rankLabel}}</div>
        <div class="leaderboard-name">${{escapeHtml(name)}}</div>
        <div class="leaderboard-score">${{score}}</div>
      `;

      section.appendChild(item);
    }});

    table.appendChild(section);
  }});
}}

async function showLeaderboard() {{
  document.getElementById("finalSummary").style.display = "none";
  document.getElementById("leaderboardScreen").style.display = "block";

  const table = document.getElementById("leaderboardTable");
  const rankDisplay = document.getElementById("leaderboardRankDisplay");
  table.innerHTML = `<div class="leaderboard-empty">Loading leaderboard...</div>`;
  rankDisplay.textContent = lastCompletedGameRow ? "Checking your rank..." : "";

  try {{
    const data = await loadLeaderboardData();
    renderLeaderboard(data);
    updateLeaderboardRank(data);
    resizeStreamlitFrame();
  }} catch (err) {{
    console.error(err);
    rankDisplay.textContent = lastCompletedGameRow ? "Rank unavailable right now." : "";
    table.innerHTML = `<div class="leaderboard-empty">Could not load leaderboard.</div>`;
    resizeStreamlitFrame();
  }}
}}

function backToFinalResults() {{
  document.getElementById("leaderboardScreen").style.display = "none";
  document.getElementById("finalSummary").style.display = "block";
  resizeStreamlitFrame();
}}

</script>
"""

left_spacer, main_col, right_spacer = st.columns([1.6, 6, 1.0])

with main_col:
    components.html(html, height=980, scrolling=False)
