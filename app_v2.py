import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Muerte celular en la infección", page_icon="🧬", layout="wide")
st.title("🧬 Muerte celular en la infección")
st.caption("Puzzle molecular interactivo · Nivel 1: apoptosis extrínseca")

html = r"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
*{box-sizing:border-box}
body{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f6f8fb;color:#17212b}
.wrap{padding:16px}
.top{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:14px}
.title{font-size:24px;font-weight:800}
.score{background:#fff;border:1px solid #d9dee5;border-radius:12px;padding:10px 14px;font-weight:800}
.instructions{background:#eef5ff;border-left:5px solid #4c7bd9;padding:12px 14px;border-radius:12px;margin-bottom:14px}
.layout{display:grid;grid-template-columns:320px 1fr;gap:16px}
.panel{background:#fff;border:1px solid #d9dee5;border-radius:16px;padding:16px}
.panel h3{margin-top:0}
.piece{border:2px solid #e7a83b;background:#fff7e8;border-radius:12px;padding:10px;margin:8px 0;font-weight:800;text-align:center;cursor:grab}
.piece:hover{transform:scale(1.01)}
.cell{border-radius:28px;overflow:hidden;border:2px solid #b9c4cf;background:#fff}
.zone-title{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#5d6a76;margin-bottom:8px}
.extracellular{background:#fff7f0;padding:16px}
.membrane{background:linear-gradient(90deg,#f8ccd0,#f4d8dc);padding:12px 16px;border-top:2px solid #eab7bc;border-bottom:2px solid #eab7bc}
.cytoplasm{background:#eef6ff;padding:18px}
.row{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap}
.arrow{font-size:25px;font-weight:800;color:#3b4a5a;margin:3px 0;text-align:center}
.slot{min-width:180px;min-height:74px;border:2px dashed #98a5b3;border-radius:14px;background:#ffffffd8;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px;font-weight:700}
.slot.correct{border:2px solid #2f9e44;background:#e9f8ec}
.slot.wrong{border:2px solid #d9485f;background:#fff0f2}
.locked{border:2px solid #8f96a3;background:#f1f3f5;color:#6b7280}
.branch{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:8px}
.branchbox{border:1px solid #cfd7df;border-radius:16px;padding:14px;background:#ffffffa8}
.branch-title{font-weight:800;margin-bottom:8px}
.feedback{margin-top:14px;padding:14px;border-radius:12px;border:1px solid #d9dee5;background:#fff;min-height:86px}
.success{color:#237a35;font-weight:800}
.error{color:#c92a2a;font-weight:800}
.hint{color:#4d5964}
.morph{margin-top:14px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.morph-step{border:1px solid #d6dde4;border-radius:12px;padding:10px;text-align:center;background:#fff}
.morph-step .icon{font-size:28px}
button{border:0;border-radius:10px;padding:10px 14px;font-weight:800;cursor:pointer;margin-top:12px;margin-right:8px}
.primary{background:#263b5e;color:#fff}
.secondary{background:#6c757d;color:#fff}
.question{margin-top:14px;border:1px solid #d7dde4;border-radius:14px;padding:14px;background:#fff}
.option{display:block;width:100%;text-align:left;margin:6px 0;background:#f3f6f9;color:#17212b}
.option.correct-answer{background:#e9f8ec;color:#14532d}
.option.wrong-answer{background:#fff0f2;color:#9f1239}
@media(max-width:950px){.layout{grid-template-columns:1fr}.branch{grid-template-columns:1fr}.morph{grid-template-columns:1fr 1fr}}
</style>
</head>
<body>
<div class="wrap">
<div class="top">
  <div class="title">Nivel 1 · Vía extrínseca de apoptosis</div>
  <div class="score">Puntaje: <span id="score">0</span>/800</div>
</div>

<div class="instructions">
  Arrastra cada componente hacia su ubicación correcta dentro de la célula. Cada acierto activa una explicación funcional.
</div>

<div class="layout">
  <div class="panel">
    <h3>🧩 Piezas moleculares</h3>
    <div id="piecebox"></div>
  </div>

  <div class="panel">
    <div class="cell">

      <div class="extracellular">
        <div class="zone-title">Medio extracelular</div>
        <div class="row">
          <div class="slot" data-answer="Ligando de muerte">TNF-α / FasL / TRAIL</div>
        </div>
      </div>

      <div class="membrane">
        <div class="zone-title">Membrana plasmática</div>
        <div class="row">
          <div class="slot" data-answer="Receptor de muerte">TNFR1 / FAS / DR</div>
        </div>
      </div>

      <div class="cytoplasm">
        <div class="zone-title">Citoplasma</div>

        <div class="row"><div class="slot" data-answer="FADD / TRADD">Adaptadores</div></div>
        <div class="arrow">↓</div>
        <div class="row"><div class="slot" data-answer="DISC">Complejo DISC</div></div>
        <div class="arrow">↓</div>
        <div class="row"><div class="slot" data-answer="Procaspasa-8 / -10">Procaspasas iniciadoras</div></div>
        <div class="arrow">↓</div>
        <div class="row"><div class="slot" data-answer="Caspasa-8 / -10">Caspasas iniciadoras activas</div></div>

        <div class="branch">
          <div class="branchbox">
            <div class="branch-title">Ruta ejecutora</div>
            <div class="arrow">↓</div>
            <div class="row"><div class="slot" data-answer="Caspasa-3 / -7">Caspasas ejecutoras</div></div>
            <div class="arrow">↓</div>
            <div class="row"><div class="slot" data-answer="Apoptosis">Desenlace</div></div>
          </div>

          <div class="branchbox">
            <div class="branch-title">Conexión mitocondrial</div>
            <div class="arrow">↘</div>
            <div class="row"><div class="slot locked">🔒 BID → tBID</div></div>
            <div style="margin-top:10px;color:#6b7280;text-align:center">Se desbloquea en el Nivel 3</div>
          </div>
        </div>
      </div>
    </div>

    <div class="feedback" id="feedback">
      <b>Retroalimentación</b><br>
      <span class="hint">Comienza por identificar la señal extracelular.</span>
    </div>

    <div class="morph">
      <div class="morph-step"><div class="icon">🔹</div><b>Contracción celular</b></div>
      <div class="morph-step"><div class="icon">🧬</div><b>Condensación de cromatina</b></div>
      <div class="morph-step"><div class="icon">🫧</div><b>Blebbing</b></div>
      <div class="morph-step"><div class="icon">⚪⚪</div><b>Cuerpos apoptóticos</b></div>
    </div>

    <button class="primary" onclick="checkLevel()">Comprobar nivel</button>
    <button class="secondary" onclick="resetLevel()">Reiniciar</button>

    <div class="question" id="challenge" style="display:none">
      <b>Desafío final</b><br>
      La caspasa-8 también puede amplificar la apoptosis a través de la mitocondria. ¿Qué proteína conecta ambas vías?
      <div>
        <button class="option" onclick="answerChallenge(this,'BID')">BID</button>
        <button class="option" onclick="answerChallenge(this,'APAF-1')">APAF-1</button>
        <button class="option" onclick="answerChallenge(this,'Caspasa-1')">Caspasa-1</button>
        <button class="option" onclick="answerChallenge(this,'BCL-2')">BCL-2</button>
      </div>
      <div id="challengeFeedback"></div>
    </div>
  </div>
</div>
</div>

<script>
const piecesData = [
  {name:"Ligando de muerte", info:"TNF-α, FasL y TRAIL son ligandos que activan receptores de muerte en la superficie celular."},
  {name:"Receptor de muerte", info:"Receptores como TNFR1 y FAS transmiten la señal apoptótica desde la membrana plasmática."},
  {name:"FADD / TRADD", info:"FADD y TRADD actúan como proteínas adaptadoras que conectan el receptor con la maquinaria de caspasas."},
  {name:"DISC", info:"El DISC es el complejo de señalización inducido por muerte que favorece el reclutamiento de procaspasas iniciadoras."},
  {name:"Procaspasa-8 / -10", info:"Son formas inactivas de caspasas iniciadoras que son reclutadas y activadas en el complejo de señalización."},
  {name:"Caspasa-8 / -10", info:"Son caspasas iniciadoras activas. Pueden activar caspasas ejecutoras y también amplificar la señal mediante BID."},
  {name:"Caspasa-3 / -7", info:"Son caspasas ejecutoras que procesan múltiples sustratos celulares y generan los cambios morfológicos de la apoptosis."},
  {name:"Apoptosis", info:"La apoptosis produce contracción celular, condensación de cromatina, blebbing y cuerpos apoptóticos sin liberación masiva del contenido celular."}
];

let score = 0;
let used = new Set();

function shuffle(a){ return [...a].sort(()=>Math.random()-0.5); }

function renderPieces(){
  const box=document.getElementById("piecebox");
  box.innerHTML="";
  shuffle(piecesData).forEach(p=>{
    const el=document.createElement("div");
    el.className="piece";
    el.draggable=true;
    el.textContent=p.name;
    el.dataset.name=p.name;
    el.addEventListener("dragstart",e=>{
      e.dataTransfer.setData("text/plain",p.name);
    });
    box.appendChild(el);
  });
}

document.querySelectorAll(".slot[data-answer]").forEach(slot=>{
  slot.addEventListener("dragover",e=>e.preventDefault());
  slot.addEventListener("drop",e=>{
    e.preventDefault();
    const name=e.dataTransfer.getData("text/plain");
    const piece=piecesData.find(x=>x.name===name);
    if(!piece) return;

    if(slot.dataset.answer===name){
      if(!used.has(name)){
        score+=100;
        used.add(name);
      }
      slot.className="slot correct";
      slot.innerHTML="<b>"+name+"</b>";
      const original=[...document.querySelectorAll(".piece")].find(x=>x.dataset.name===name);
      if(original) original.remove();
      document.getElementById("score").textContent=score;
      document.getElementById("feedback").innerHTML=
        '<span class="success">✓ Correcto.</span><br>'+piece.info;
    }else{
      slot.classList.add("wrong");
      setTimeout(()=>slot.classList.remove("wrong"),700);
      document.getElementById("feedback").innerHTML=
        '<span class="error">✗ Incorrecto.</span><br>'+
        '<span class="hint">Piensa en la secuencia molecular y en la ubicación celular del componente.</span>';
    }
  });
});

function checkLevel(){
  if(used.size===8){
    document.getElementById("feedback").innerHTML=
      '<span class="success">🏆 Nivel completado.</span><br>'+
      'Has reconstruido correctamente la vía extrínseca de apoptosis.';
    document.getElementById("challenge").style.display="block";
  }else{
    document.getElementById("feedback").innerHTML=
      '<span class="hint">Aún faltan '+(8-used.size)+' piezas por ubicar.</span>';
  }
}

function answerChallenge(btn,ans){
  document.querySelectorAll(".option").forEach(b=>b.classList.remove("correct-answer","wrong-answer"));
  const fb=document.getElementById("challengeFeedback");
  if(ans==="BID"){
    btn.classList.add("correct-answer");
    fb.innerHTML='<span class="success">✓ Correcto.</span> La caspasa-8 puede escindir BID para generar tBID, que conecta la vía extrínseca con la vía mitocondrial.';
  }else{
    btn.classList.add("wrong-answer");
    fb.innerHTML='<span class="error">✗ No.</span> Busca una proteína BH3-only que conecte la señal de caspasa-8 con la mitocondria.';
  }
}

function resetLevel(){ location.reload(); }

renderPieces();
</script>
</body>
</html>
"""

components.html(html, height=1180, scrolling=True)
