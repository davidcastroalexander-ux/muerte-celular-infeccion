import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Muerte celular en la infección", page_icon="🧬", layout="wide")
st.title("🧬 Muerte celular en la infección")
st.caption("Puzzle molecular interactivo · Apoptosis, piroptosis y autofagia")

nivel = st.radio(
    "Selecciona el nivel",
    ["Nivel 1 · Vía extrínseca", "Nivel 2 · Vía intrínseca", "Nivel 3 · Conexión BID–tBID", "Nivel 4 · Piroptosis", "Nivel 5 · Autofagia", "Nivel 6 · Compara las respuestas celulares", "Nivel 7 · Patógeno → respuesta celular"],
    horizontal=True,
)

if nivel == "Nivel 1 · Vía extrínseca":
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

elif nivel == "Nivel 2 · Vía intrínseca":
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
.piece{border:2px solid #6f8dd6;background:#eef4ff;border-radius:12px;padding:10px;margin:8px 0;font-weight:800;text-align:center;cursor:grab}
.piece:hover{transform:scale(1.01)}
.cell{border-radius:28px;overflow:hidden;border:2px solid #b9c4cf;background:#fff}
.zone-title{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#5d6a76;margin-bottom:8px}
.cytoplasm{background:#eef6ff;padding:18px}
.mitozone{background:#f4f7f8;padding:18px;border-top:1px solid #d6dde4;border-bottom:1px solid #d6dde4}
.row{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap}
.arrow{font-size:25px;font-weight:800;color:#3b4a5a;margin:3px 0;text-align:center}
.slot{min-width:190px;min-height:72px;border:2px dashed #98a5b3;border-radius:14px;background:#ffffffd8;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px;font-weight:700}
.slot.correct{border:2px solid #2f9e44;background:#e9f8ec}
.slot.wrong{border:2px solid #d9485f;background:#fff0f2}
.branch{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:12px 0}
.branchbox{border:1px solid #cfd7df;border-radius:16px;padding:14px;background:#ffffffa8}
.branch-title{font-weight:800;margin-bottom:8px;text-align:center}
.feedback{margin-top:14px;padding:14px;border-radius:12px;border:1px solid #d9dee5;background:#fff;min-height:92px}
.success{color:#237a35;font-weight:800}.error{color:#c92a2a;font-weight:800}.hint{color:#4d5964}
button{border:0;border-radius:10px;padding:10px 14px;font-weight:800;cursor:pointer;margin-top:12px;margin-right:8px}
.primary{background:#263b5e;color:#fff}.secondary{background:#6c757d;color:#fff}
.question{margin-top:14px;border:1px solid #d7dde4;border-radius:14px;padding:14px;background:#fff}
.option{display:block;width:100%;text-align:left;margin:6px 0;background:#f3f6f9;color:#17212b}
.option.correct-answer{background:#e9f8ec;color:#14532d}.option.wrong-answer{background:#fff0f2;color:#9f1239}
.mito{font-size:56px;text-align:center;margin:4px 0}
@media(max-width:950px){.layout{grid-template-columns:1fr}.branch{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="wrap">
<div class="top">
  <div class="title">Nivel 2 · Vía intrínseca / mitocondrial</div>
  <div class="score">Puntaje: <span id="score">0</span>/1000</div>
</div>

<div class="instructions">
  Reconstruye la vía intrínseca de apoptosis. En este nivel no solo hay activadores: también debes reconocer reguladores inhibitorios.
</div>

<div class="layout">
  <div class="panel">
    <h3>🧩 Piezas moleculares</h3>
    <div id="piecebox"></div>
  </div>

  <div class="panel">
    <div class="cell">

      <div class="cytoplasm">
        <div class="zone-title">Estímulos intracelulares</div>
        <div class="row">
          <div class="slot" data-answer="Estrés intracelular">Daño del ADN / estrés del RE / hipoxia / estrés metabólico</div>
        </div>
        <div class="arrow">↓</div>
        <div class="row">
          <div class="slot" data-answer="Proteínas BH3-only">Proteínas BH3-only</div>
        </div>

        <div class="branch">
          <div class="branchbox">
            <div class="branch-title">Regulación antiapoptótica</div>
            <div class="row">
              <div class="slot" data-answer="BCL-2 / BCL-XL / MCL1">Proteínas antiapoptóticas</div>
            </div>
          </div>

          <div class="branchbox">
            <div class="branch-title">Activación proapoptótica</div>
            <div class="row">
              <div class="slot" data-answer="BAX / BAK">BAX / BAK</div>
            </div>
          </div>
        </div>

        <div class="arrow">↓</div>
      </div>

      <div class="mitozone">
        <div class="zone-title">Mitocondria</div>
        <div class="mito">🫘</div>
        <div class="row">
          <div class="slot" data-answer="MOMP">Permeabilización de la membrana externa mitocondrial</div>
        </div>
        <div class="arrow">↓</div>

        <div class="branch">
          <div class="branchbox">
            <div class="branch-title">Liberación mitocondrial 1</div>
            <div class="row">
              <div class="slot" data-answer="Citocromo c">Citocromo c</div>
            </div>
          </div>

          <div class="branchbox">
            <div class="branch-title">Liberación mitocondrial 2</div>
            <div class="row">
              <div class="slot" data-answer="SMAC / DIABLO">SMAC / DIABLO</div>
            </div>
          </div>
        </div>
      </div>

      <div class="cytoplasm">
        <div class="row">
          <div class="slot" data-answer="APAF-1">APAF-1</div>
        </div>
        <div class="arrow">↓</div>
        <div class="row">
          <div class="slot" data-answer="Apoptosoma">Apoptosoma</div>
        </div>
        <div class="arrow">↓</div>
        <div class="row">
          <div class="slot" data-answer="Caspasa-9">Caspasa-9</div>
        </div>

        <div class="branch">
          <div class="branchbox">
            <div class="branch-title">Ejecución</div>
            <div class="row">
              <div class="slot" data-answer="Caspasa-3 / -7">Caspasa-3 / -7</div>
            </div>
          </div>

          <div class="branchbox">
            <div class="branch-title">Control de caspasas</div>
            <div class="row">
              <div class="slot" data-answer="XIAP">XIAP</div>
            </div>
          </div>
        </div>

        <div class="arrow">↓</div>
        <div class="row">
          <div class="slot" data-answer="Apoptosis">Apoptosis</div>
        </div>
      </div>

    </div>

    <div class="feedback" id="feedback">
      <b>Retroalimentación</b><br>
      <span class="hint">Comienza con el estímulo intracelular que activa proteínas BH3-only.</span>
    </div>

    <button class="primary" onclick="checkLevel()">Comprobar nivel</button>
    <button class="secondary" onclick="location.reload()">Reiniciar</button>

    <div class="question" id="challenge" style="display:none">
      <b>Desafío final</b><br>
      ¿Qué evento constituye el punto decisivo que permite la liberación de citocromo c desde la mitocondria?
      <div>
        <button class="option" onclick="answerChallenge(this,'MOMP')">MOMP</button>
        <button class="option" onclick="answerChallenge(this,'DISC')">Formación del DISC</button>
        <button class="option" onclick="answerChallenge(this,'Caspasa-1')">Activación de caspasa-1</button>
        <button class="option" onclick="answerChallenge(this,'NF-kB')">Activación de NF-κB</button>
      </div>
      <div id="challengeFeedback"></div>
    </div>
  </div>
</div>
</div>

<script>
const piecesData=[
{name:"Estrés intracelular",info:"Daño del ADN, estrés del retículo endoplásmico, hipoxia y estrés metabólico pueden activar la vía intrínseca."},
{name:"Proteínas BH3-only",info:"Las proteínas BH3-only funcionan como sensores de estrés y favorecen la activación de la maquinaria proapoptótica."},
{name:"BCL-2 / BCL-XL / MCL1",info:"Estas proteínas antiapoptóticas restringen la activación de BAX y BAK y ayudan a preservar la integridad mitocondrial."},
{name:"BAX / BAK",info:"BAX y BAK son efectores proapoptóticos que oligomerizan en la membrana externa mitocondrial."},
{name:"MOMP",info:"La permeabilización de la membrana externa mitocondrial permite la salida de proteínas proapoptóticas al citosol."},
{name:"Citocromo c",info:"El citocromo c liberado al citosol se asocia con APAF-1 y favorece la formación del apoptosoma."},
{name:"SMAC / DIABLO",info:"SMAC/DIABLO favorece la apoptosis al antagonizar proteínas inhibidoras de apoptosis como XIAP."},
{name:"APAF-1",info:"APAF-1 es un componente central de la plataforma que forma el apoptosoma."},
{name:"Apoptosoma",info:"El apoptosoma recluta y activa caspasa-9."},
{name:"Caspasa-9",info:"Caspasa-9 es la caspasa iniciadora característica de la vía mitocondrial."},
{name:"Caspasa-3 / -7",info:"Las caspasas ejecutoras procesan múltiples sustratos y producen los cambios morfológicos de la apoptosis."},
{name:"XIAP",info:"XIAP inhibe caspasas; su acción puede ser contrarrestada por SMAC/DIABLO."},
{name:"Apoptosis",info:"Desenlace final con contracción celular, condensación de cromatina y formación de cuerpos apoptóticos."}
];
let score=0, used=new Set();

function shuffle(a){return [...a].sort(()=>Math.random()-0.5)}

function renderPieces(){
 const box=document.getElementById("piecebox");
 box.innerHTML="";
 shuffle(piecesData).forEach(p=>{
   const el=document.createElement("div");
   el.className="piece";
   el.draggable=true;
   el.textContent=p.name;
   el.dataset.name=p.name;
   el.addEventListener("dragstart",e=>e.dataTransfer.setData("text/plain",p.name));
   box.appendChild(el);
 });
}

document.querySelectorAll(".slot[data-answer]").forEach(slot=>{
 slot.addEventListener("dragover",e=>e.preventDefault());
 slot.addEventListener("drop",e=>{
   e.preventDefault();
   const name=e.dataTransfer.getData("text/plain");
   const piece=piecesData.find(x=>x.name===name);
   if(!piece)return;

   if(slot.dataset.answer===name){
     if(!used.has(name)){score+=100;used.add(name)}
     slot.className="slot correct";
     slot.innerHTML="<b>"+name+"</b>";
     const original=[...document.querySelectorAll(".piece")].find(x=>x.dataset.name===name);
     if(original)original.remove();
     document.getElementById("score").textContent=score;
     document.getElementById("feedback").innerHTML='<span class="success">✓ Correcto.</span><br>'+piece.info;
   }else{
     slot.classList.add("wrong");
     setTimeout(()=>slot.classList.remove("wrong"),700);
     document.getElementById("feedback").innerHTML='<span class="error">✗ Incorrecto.</span><br><span class="hint">Piensa si esta molécula activa, inhibe o ejecuta la apoptosis y dónde actúa.</span>';
   }
 });
});

function checkLevel(){
 if(used.size===piecesData.length){
   document.getElementById("feedback").innerHTML='<span class="success">🏆 Nivel completado.</span><br>Has reconstruido correctamente la vía intrínseca de apoptosis.';
   document.getElementById("challenge").style.display="block";
 }else{
   document.getElementById("feedback").innerHTML='<span class="hint">Aún faltan '+(piecesData.length-used.size)+' piezas.</span>';
 }
}

function answerChallenge(btn,ans){
 document.querySelectorAll(".option").forEach(b=>b.classList.remove("correct-answer","wrong-answer"));
 const fb=document.getElementById("challengeFeedback");
 if(ans==="MOMP"){
   btn.classList.add("correct-answer");
   fb.innerHTML='<span class="success">✓ Correcto.</span> MOMP permite la liberación de citocromo c y otras proteínas mitocondriales proapoptóticas.';
 }else{
   btn.classList.add("wrong-answer");
   fb.innerHTML='<span class="error">✗ Incorrecto.</span> Busca el evento que altera directamente la membrana externa mitocondrial.';
 }
}

renderPieces();
</script>
</body>
</html>
"""
    components.html(html, height=1550, scrolling=True)


elif nivel == "Nivel 3 · Conexión BID–tBID":
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
.piece{border:2px solid #8d6ccf;background:#f6f0ff;border-radius:12px;padding:10px;margin:8px 0;font-weight:800;text-align:center;cursor:grab}
.piece:hover{transform:scale(1.01)}
.cell{border-radius:28px;overflow:hidden;border:2px solid #b9c4cf;background:#fff}
.zone-title{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#5d6a76;margin-bottom:8px}
.extracellular{background:#fff7f0;padding:14px}
.membrane{background:linear-gradient(90deg,#f8ccd0,#f4d8dc);padding:12px 16px;border-top:2px solid #eab7bc;border-bottom:2px solid #eab7bc}
.cytoplasm{background:#eef6ff;padding:18px}
.mitozone{background:#f7f3ff;padding:18px;border-top:1px solid #d8ccee;border-bottom:1px solid #d8ccee}
.row{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap}
.arrow{font-size:25px;font-weight:800;color:#3b4a5a;margin:3px 0;text-align:center}
.slot{min-width:190px;min-height:72px;border:2px dashed #98a5b3;border-radius:14px;background:#ffffffd8;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px;font-weight:700}
.slot.correct{border:2px solid #2f9e44;background:#e9f8ec}
.slot.wrong{border:2px solid #d9485f;background:#fff0f2}
.bridge{display:grid;grid-template-columns:1fr 70px 1fr;gap:10px;align-items:center;margin:12px 0}
.side{border:1px solid #cfd7df;border-radius:16px;padding:14px;background:#ffffffa8}
.side-title{text-align:center;font-weight:800;margin-bottom:8px}
.feedback{margin-top:14px;padding:14px;border-radius:12px;border:1px solid #d9dee5;background:#fff;min-height:92px}
.success{color:#237a35;font-weight:800}.error{color:#c92a2a;font-weight:800}.hint{color:#4d5964}
button{border:0;border-radius:10px;padding:10px 14px;font-weight:800;cursor:pointer;margin-top:12px;margin-right:8px}
.primary{background:#263b5e;color:#fff}.secondary{background:#6c757d;color:#fff}
.question{margin-top:14px;border:1px solid #d7dde4;border-radius:14px;padding:14px;background:#fff}
.option{display:block;width:100%;text-align:left;margin:6px 0;background:#f3f6f9;color:#17212b}
.option.correct-answer{background:#e9f8ec;color:#14532d}.option.wrong-answer{background:#fff0f2;color:#9f1239}
.summary{margin-top:14px;padding:14px;border-radius:14px;background:#f9fafb;border:1px solid #d9dee5}
@media(max-width:950px){.layout{grid-template-columns:1fr}.bridge{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="wrap">
<div class="top">
  <div class="title">Nivel 3 · Conexión entre vía extrínseca e intrínseca</div>
  <div class="score">Puntaje: <span id="score">0</span>/900</div>
</div>

<div class="instructions">
  Reconstruye el puente molecular mediante el cual la caspasa-8 amplifica la señal apoptótica a través de la mitocondria.
</div>

<div class="layout">
  <div class="panel">
    <h3>🧩 Piezas moleculares</h3>
    <div id="piecebox"></div>
  </div>

  <div class="panel">
    <div class="cell">
      <div class="extracellular">
        <div class="zone-title">Señal extrínseca ya activada</div>
        <div class="row">
          <div class="slot" data-answer="Caspasa-8 activa">Caspasa iniciadora activa</div>
        </div>
      </div>

      <div class="cytoplasm">
        <div class="zone-title">Puente molecular</div>
        <div class="arrow">↓</div>
        <div class="row">
          <div class="slot" data-answer="BID">Proteína BH3-only</div>
        </div>
        <div class="arrow">↓ escisión</div>
        <div class="row">
          <div class="slot" data-answer="tBID">Forma truncada activa</div>
        </div>
        <div class="arrow">↓</div>

        <div class="bridge">
          <div class="side">
            <div class="side-title">Regulación</div>
            <div class="row">
              <div class="slot" data-answer="BCL-2 / BCL-XL">Freno antiapoptótico</div>
            </div>
          </div>

          <div class="arrow">⇢</div>

          <div class="side">
            <div class="side-title">Activación mitocondrial</div>
            <div class="row">
              <div class="slot" data-answer="BAX / BAK">Efectores proapoptóticos</div>
            </div>
          </div>
        </div>

        <div class="arrow">↓</div>
      </div>

      <div class="mitozone">
        <div class="zone-title">Mitocondria</div>
        <div class="row">
          <div class="slot" data-answer="MOMP">Permeabilización de membrana externa</div>
        </div>
        <div class="arrow">↓</div>
        <div class="row">
          <div class="slot" data-answer="Citocromo c">Liberación mitocondrial</div>
        </div>
      </div>

      <div class="cytoplasm">
        <div class="arrow">↓</div>
        <div class="row">
          <div class="slot" data-answer="Apoptosoma / Caspasa-9">Amplificación de la vía intrínseca</div>
        </div>
        <div class="arrow">↓</div>
        <div class="row">
          <div class="slot" data-answer="Caspasa-3 / -7">Caspasas ejecutoras</div>
        </div>
        <div class="arrow">↓</div>
        <div class="row">
          <div class="slot" data-answer="Apoptosis">Desenlace final</div>
        </div>
      </div>
    </div>

    <div class="feedback" id="feedback">
      <b>Retroalimentación</b><br>
      <span class="hint">La clave de este nivel es descubrir cómo caspasa-8 comunica la vía extrínseca con la mitocondria.</span>
    </div>

    <button class="primary" onclick="checkLevel()">Comprobar nivel</button>
    <button class="secondary" onclick="location.reload()">Reiniciar</button>

    <div class="question" id="challenge" style="display:none">
      <b>Desafío final</b><br>
      ¿Cuál es la función principal de tBID en esta conexión?
      <div>
        <button class="option" onclick="answerChallenge(this,'activar')">Favorecer la activación de BAX/BAK y la MOMP</button>
        <button class="option" onclick="answerChallenge(this,'inhibir')">Inhibir directamente caspasa-9</button>
        <button class="option" onclick="answerChallenge(this,'inflam')">Formar el inflamasoma</button>
        <button class="option" onclick="answerChallenge(this,'autof')">Iniciar la formación del autofagosoma</button>
      </div>
      <div id="challengeFeedback"></div>
    </div>

    <div class="summary">
      <b>Idea clave:</b> la vía extrínseca no siempre termina de forma aislada. La caspasa-8 puede escindir BID a tBID,
      y esta señal favorece la activación mitocondrial, amplificando la apoptosis.
    </div>
  </div>
</div>
</div>

<script>
const piecesData=[
{name:"Caspasa-8 activa",info:"La caspasa-8 es una caspasa iniciadora de la vía extrínseca y puede conectar con la mitocondria mediante BID."},
{name:"BID",info:"BID es una proteína BH3-only que sirve como punto de conexión entre las vías extrínseca e intrínseca."},
{name:"tBID",info:"La caspasa-8 escinde BID y genera tBID, una forma activa que favorece la señal proapoptótica mitocondrial."},
{name:"BCL-2 / BCL-XL",info:"Estas proteínas antiapoptóticas se oponen a la activación de la maquinaria mitocondrial de apoptosis."},
{name:"BAX / BAK",info:"BAX y BAK son efectores proapoptóticos cuya activación conduce a la permeabilización de la membrana externa mitocondrial."},
{name:"MOMP",info:"MOMP permite la liberación de proteínas mitocondriales proapoptóticas al citosol."},
{name:"Citocromo c",info:"El citocromo c liberado participa en la formación del apoptosoma junto con APAF-1."},
{name:"Apoptosoma / Caspasa-9",info:"La formación del apoptosoma promueve la activación de caspasa-9 y amplifica la cascada apoptótica."},
{name:"Caspasa-3 / -7",info:"Las caspasas ejecutoras procesan numerosos sustratos celulares y producen los cambios morfológicos de la apoptosis."},
{name:"Apoptosis",info:"El desenlace es una muerte celular programada con fragmentación nuclear, contracción celular y cuerpos apoptóticos."}
];
let score=0,used=new Set();

function shuffle(a){return [...a].sort(()=>Math.random()-0.5)}

function renderPieces(){
 const box=document.getElementById("piecebox");
 box.innerHTML="";
 shuffle(piecesData).forEach(p=>{
  const el=document.createElement("div");
  el.className="piece"; el.draggable=true; el.textContent=p.name; el.dataset.name=p.name;
  el.addEventListener("dragstart",e=>e.dataTransfer.setData("text/plain",p.name));
  box.appendChild(el);
 });
}

document.querySelectorAll(".slot[data-answer]").forEach(slot=>{
 slot.addEventListener("dragover",e=>e.preventDefault());
 slot.addEventListener("drop",e=>{
  e.preventDefault();
  const name=e.dataTransfer.getData("text/plain");
  const piece=piecesData.find(x=>x.name===name);
  if(!piece)return;

  if(slot.dataset.answer===name){
    if(!used.has(name)){score+=90;used.add(name)}
    slot.className="slot correct";
    slot.innerHTML="<b>"+name+"</b>";
    const original=[...document.querySelectorAll(".piece")].find(x=>x.dataset.name===name);
    if(original)original.remove();
    document.getElementById("score").textContent=score;
    document.getElementById("feedback").innerHTML='<span class="success">✓ Correcto.</span><br>'+piece.info;
  }else{
    slot.classList.add("wrong");
    setTimeout(()=>slot.classList.remove("wrong"),700);
    document.getElementById("feedback").innerHTML='<span class="error">✗ Incorrecto.</span><br><span class="hint">Piensa si este componente pertenece a la vía extrínseca, al puente BID/tBID o a la amplificación mitocondrial.</span>';
  }
 });
});

function checkLevel(){
 if(used.size===piecesData.length){
   document.getElementById("feedback").innerHTML='<span class="success">🏆 Nivel completado.</span><br>Has conectado correctamente la vía extrínseca con la vía mitocondrial mediante BID/tBID.';
   document.getElementById("challenge").style.display="block";
 }else{
   document.getElementById("feedback").innerHTML='<span class="hint">Aún faltan '+(piecesData.length-used.size)+' piezas.</span>';
 }
}

function answerChallenge(btn,ans){
 document.querySelectorAll(".option").forEach(b=>b.classList.remove("correct-answer","wrong-answer"));
 const fb=document.getElementById("challengeFeedback");
 if(ans==="activar"){
   btn.classList.add("correct-answer");
   fb.innerHTML='<span class="success">✓ Correcto.</span> tBID favorece la activación de BAX/BAK, promoviendo MOMP y amplificando la señal apoptótica.';
 }else{
   btn.classList.add("wrong-answer");
   fb.innerHTML='<span class="error">✗ Incorrecto.</span> tBID pertenece a la conexión proapoptótica hacia la mitocondria.';
 }
}

renderPieces();
</script>
</body>
</html>
"""
    components.html(html, height=1540, scrolling=True)


elif nivel == "Nivel 4 · Piroptosis":
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
.instructions{background:#fff3e6;border-left:5px solid #f08c00;padding:12px 14px;border-radius:12px;margin-bottom:14px}
.layout{display:grid;grid-template-columns:320px 1fr;gap:16px}
.panel{background:#fff;border:1px solid #d9dee5;border-radius:16px;padding:16px}
.panel h3{margin-top:0}
.piece{border:2px solid #e67700;background:#fff4e6;border-radius:12px;padding:10px;margin:8px 0;font-weight:800;text-align:center;cursor:grab}
.piece:hover{transform:scale(1.01)}
.cell{border-radius:28px;overflow:hidden;border:2px solid #b9c4cf;background:#fff}
.zone-title{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#5d6a76;margin-bottom:8px}
.cytoplasm{background:#fff8f0;padding:18px}
.nucleus{background:#fff3bf;padding:14px;border-top:1px solid #f1d68a;border-bottom:1px solid #f1d68a}
.row{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap}
.arrow{font-size:25px;font-weight:800;color:#3b4a5a;margin:3px 0;text-align:center}
.slot{min-width:190px;min-height:72px;border:2px dashed #98a5b3;border-radius:14px;background:#ffffffd8;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px;font-weight:700}
.slot.correct{border:2px solid #2f9e44;background:#e9f8ec}
.slot.wrong{border:2px solid #d9485f;background:#fff0f2}
.branch{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:12px 0}
.branchbox{border:1px solid #cfd7df;border-radius:16px;padding:14px;background:#ffffffa8}
.branch-title{font-weight:800;margin-bottom:8px;text-align:center}
.feedback{margin-top:14px;padding:14px;border-radius:12px;border:1px solid #d9dee5;background:#fff;min-height:92px}
.success{color:#237a35;font-weight:800}.error{color:#c92a2a;font-weight:800}.hint{color:#4d5964}
button{border:0;border-radius:10px;padding:10px 14px;font-weight:800;cursor:pointer;margin-top:12px;margin-right:8px}
.primary{background:#263b5e;color:#fff}.secondary{background:#6c757d;color:#fff}
.question{margin-top:14px;border:1px solid #d7dde4;border-radius:14px;padding:14px;background:#fff}
.option{display:block;width:100%;text-align:left;margin:6px 0;background:#f3f6f9;color:#17212b}
.option.correct-answer{background:#e9f8ec;color:#14532d}.option.wrong-answer{background:#fff0f2;color:#9f1239}
.morph{margin-top:14px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.morph-step{border:1px solid #d6dde4;border-radius:12px;padding:10px;text-align:center;background:#fff}
.morph-step .icon{font-size:28px}
.summary{margin-top:14px;padding:14px;border-radius:14px;background:#fff9db;border:1px solid #ffe066}
@media(max-width:950px){.layout{grid-template-columns:1fr}.branch{grid-template-columns:1fr}.morph{grid-template-columns:1fr 1fr}}
</style>
</head>
<body>
<div class="wrap">
<div class="top">
  <div class="title">Nivel 4 · Piroptosis</div>
  <div class="score">Puntaje: <span id="score">0</span>/900</div>
</div>

<div class="instructions">
  Reconstruye la secuencia que conduce a una muerte celular inflamatoria dependiente de caspasa-1.
  El objetivo es distinguirla de la apoptosis.
</div>

<div class="layout">
  <div class="panel">
    <h3>🧩 Piezas moleculares</h3>
    <div id="piecebox"></div>
  </div>

  <div class="panel">
    <div class="cell">

      <div class="cytoplasm">
        <div class="zone-title">Citoplasma · reconocimiento de infección</div>
        <div class="row">
          <div class="slot" data-answer="PAMP / señal microbiana">Señal del patógeno en el citosol</div>
        </div>
        <div class="arrow">↓</div>

        <div class="row">
          <div class="slot" data-answer="NLR / sensor citosólico">Sensor intracelular</div>
        </div>
        <div class="arrow">↓</div>

        <div class="row">
          <div class="slot" data-answer="Inflamasoma">Plataforma multiproteica</div>
        </div>
        <div class="arrow">↓</div>

        <div class="row">
          <div class="slot" data-answer="Procaspasa-1">Caspasa inflamatoria inactiva</div>
        </div>
        <div class="arrow">↓ activación</div>

        <div class="row">
          <div class="slot" data-answer="Caspasa-1">Caspasa inflamatoria activa</div>
        </div>

        <div class="branch">
          <div class="branchbox">
            <div class="branch-title">Maduración de citocinas</div>
            <div class="row">
              <div class="slot" data-answer="IL-1β / IL-18 maduras">IL-1β / IL-18</div>
            </div>
          </div>

          <div class="branchbox">
            <div class="branch-title">Cambios celulares</div>
            <div class="row">
              <div class="slot" data-answer="Pérdida de integridad de membrana">Membrana permeable / ruptura</div>
            </div>
          </div>
        </div>

        <div class="arrow">↓</div>

        <div class="row">
          <div class="slot" data-answer="Liberación de contenido citoplasmático">Contenido celular al exterior</div>
        </div>
        <div class="arrow">↓</div>

        <div class="row">
          <div class="slot" data-answer="Piroptosis">Muerte celular inflamatoria</div>
        </div>
      </div>

      <div class="nucleus">
        <div class="zone-title">Cambios nucleares asociados</div>
        <div style="text-align:center;font-weight:700">
          Fragmentación de ADN y condensación nuclear pueden presentarse, pero no definen por sí solas apoptosis.
        </div>
      </div>

    </div>

    <div class="feedback" id="feedback">
      <b>Retroalimentación</b><br>
      <span class="hint">Empieza por una señal microbiana detectada en el citosol y sigue hasta caspasa-1.</span>
    </div>

    <div class="morph">
      <div class="morph-step"><div class="icon">🔥</div><b>Inflamación</b></div>
      <div class="morph-step"><div class="icon">💧</div><b>Entrada de agua / tumefacción</b></div>
      <div class="morph-step"><div class="icon">💥</div><b>Ruptura de membrana</b></div>
      <div class="morph-step"><div class="icon">📣</div><b>Liberación de mediadores</b></div>
    </div>

    <button class="primary" onclick="checkLevel()">Comprobar nivel</button>
    <button class="secondary" onclick="location.reload()">Reiniciar</button>

    <div class="question" id="challenge" style="display:none">
      <b>Desafío final</b><br>
      ¿Cuál característica permite diferenciar mejor la piroptosis de la apoptosis clásica en esta actividad?
      <div>
        <button class="option" onclick="answerChallenge(this,'ruptura')">Pérdida de integridad de membrana y liberación de contenido citoplasmático</button>
        <button class="option" onclick="answerChallenge(this,'dna')">Fragmentación del ADN</button>
        <button class="option" onclick="answerChallenge(this,'nucleo')">Condensación nuclear</button>
        <button class="option" onclick="answerChallenge(this,'c3')">Activación de caspasa-3 como evento definitorio</button>
      </div>
      <div id="challengeFeedback"></div>
    </div>

    <div class="summary">
      <b>Idea clave:</b> en el artículo base, la piroptosis se caracteriza por activación de caspasa-1,
      liberación de citocinas inflamatorias y pérdida de la integridad de la membrana plasmática.
      Puede compartir fragmentación de ADN y condensación nuclear con otras formas de muerte.
    </div>
  </div>
</div>
</div>

<script>
const piecesData=[
{name:"PAMP / señal microbiana",info:"Durante la infección, productos o señales del patógeno presentes en el citosol pueden iniciar la activación de la respuesta inflamatoria."},
{name:"NLR / sensor citosólico",info:"Los receptores citosólicos tipo NLR actúan como sensores intracelulares y pueden participar en el ensamblaje de inflamasomas."},
{name:"Inflamasoma",info:"El inflamasoma es una plataforma multiproteica que favorece el reclutamiento y activación de procaspasa-1."},
{name:"Procaspasa-1",info:"Caspasa-1 se sintetiza como un zimógeno inactivo que requiere activación."},
{name:"Caspasa-1",info:"Caspasa-1 activa participa en la maduración de citocinas inflamatorias y en la muerte celular piroptótica."},
{name:"IL-1β / IL-18 maduras",info:"La activación de caspasa-1 favorece la generación de formas maduras de citocinas proinflamatorias como IL-1β e IL-18."},
{name:"Pérdida de integridad de membrana",info:"Una característica destacada de la piroptosis es la pérdida de integridad de la membrana plasmática."},
{name:"Liberación de contenido citoplasmático",info:"La salida de contenido celular al medio extracelular contribuye al carácter altamente inflamatorio de la piroptosis."},
{name:"Piroptosis",info:"La piroptosis es una forma inflamatoria de muerte celular asociada, en el artículo base, con activación de caspasa-1."}
];
let score=0,used=new Set();

function shuffle(a){return [...a].sort(()=>Math.random()-0.5)}

function renderPieces(){
 const box=document.getElementById("piecebox");
 box.innerHTML="";
 shuffle(piecesData).forEach(p=>{
  const el=document.createElement("div");
  el.className="piece";el.draggable=true;el.textContent=p.name;el.dataset.name=p.name;
  el.addEventListener("dragstart",e=>e.dataTransfer.setData("text/plain",p.name));
  box.appendChild(el);
 });
}

document.querySelectorAll(".slot[data-answer]").forEach(slot=>{
 slot.addEventListener("dragover",e=>e.preventDefault());
 slot.addEventListener("drop",e=>{
  e.preventDefault();
  const name=e.dataTransfer.getData("text/plain");
  const piece=piecesData.find(x=>x.name===name);
  if(!piece)return;

  if(slot.dataset.answer===name){
    if(!used.has(name)){score+=100;used.add(name)}
    slot.className="slot correct";
    slot.innerHTML="<b>"+name+"</b>";
    const original=[...document.querySelectorAll(".piece")].find(x=>x.dataset.name===name);
    if(original)original.remove();
    document.getElementById("score").textContent=score;
    document.getElementById("feedback").innerHTML='<span class="success">✓ Correcto.</span><br>'+piece.info;
  }else{
    slot.classList.add("wrong");
    setTimeout(()=>slot.classList.remove("wrong"),700);
    document.getElementById("feedback").innerHTML='<span class="error">✗ Incorrecto.</span><br><span class="hint">Piensa si esta pieza pertenece al reconocimiento, activación de caspasa-1, liberación de citocinas o desenlace celular.</span>';
  }
 });
});

function checkLevel(){
 if(used.size===piecesData.length){
   document.getElementById("feedback").innerHTML='<span class="success">🏆 Nivel completado.</span><br>Has reconstruido correctamente la secuencia conceptual de piroptosis descrita en el material base.';
   document.getElementById("challenge").style.display="block";
 }else{
   document.getElementById("feedback").innerHTML='<span class="hint">Aún faltan '+(piecesData.length-used.size)+' piezas.</span>';
 }
}

function answerChallenge(btn,ans){
 document.querySelectorAll(".option").forEach(b=>b.classList.remove("correct-answer","wrong-answer"));
 const fb=document.getElementById("challengeFeedback");
 if(ans==="ruptura"){
   btn.classList.add("correct-answer");
   fb.innerHTML='<span class="success">✓ Correcto.</span> La pérdida de integridad de membrana y la liberación del contenido citoplasmático explican el carácter inflamatorio de la piroptosis.';
 }else{
   btn.classList.add("wrong-answer");
   fb.innerHTML='<span class="error">✗ Incorrecto.</span> Recuerda que fragmentación de ADN y condensación nuclear también pueden observarse en piroptosis.';
 }
}

renderPieces();
</script>
</body>
</html>
"""
    components.html(html, height=1600, scrolling=True)

elif nivel == "Nivel 5 · Autofagia":
    html = r"""
<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<style>
*{box-sizing:border-box}body{margin:0;font-family:Arial;background:#f6f8fb;color:#17212b}.wrap{padding:16px}
.top{display:flex;justify-content:space-between;align-items:center}.title{font-size:24px;font-weight:800}
.score{background:#fff;border:1px solid #ddd;border-radius:12px;padding:10px 14px;font-weight:800}
.instructions{background:#ecfdf5;border-left:5px solid #16a34a;padding:12px 14px;border-radius:12px;margin:14px 0}
.layout{display:grid;grid-template-columns:320px 1fr;gap:16px}.panel{background:#fff;border:1px solid #d9dee5;border-radius:16px;padding:16px}
.piece{border:2px solid #16a34a;background:#f0fdf4;border-radius:12px;padding:10px;margin:8px 0;font-weight:800;text-align:center;cursor:grab}
.cell{border-radius:28px;overflow:hidden;border:2px solid #b9c4cf}.cyto{background:#eefbf5;padding:18px}
.zone{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#5d6a76;margin-bottom:10px}
.row{display:flex;justify-content:center;align-items:center;gap:10px;flex-wrap:wrap}.arrow{text-align:center;font-size:25px;font-weight:800;margin:4px}
.slot{min-width:210px;min-height:72px;border:2px dashed #98a5b3;border-radius:14px;background:#fff;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px;font-weight:700}
.correct{border:2px solid #2f9e44!important;background:#e9f8ec!important}.wrong{border:2px solid #d9485f!important;background:#fff0f2!important}
.branch{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:12px 0}.box{border:1px solid #cfd7df;border-radius:16px;padding:14px;background:#fff}
.feedback,.question,.summary{margin-top:14px;padding:14px;border-radius:12px;border:1px solid #d9dee5;background:#fff}
.success{color:#237a35;font-weight:800}.error{color:#c92a2a;font-weight:800}.hint{color:#4d5964}
button{border:0;border-radius:10px;padding:10px 14px;font-weight:800;cursor:pointer;margin-top:10px;margin-right:8px}.primary{background:#263b5e;color:#fff}.secondary{background:#6c757d;color:#fff}
.option{display:block;width:100%;text-align:left;background:#f3f6f9;color:#17212b}.good{background:#e9f8ec!important;color:#14532d}.bad{background:#fff0f2!important;color:#9f1239}
@media(max-width:950px){.layout,.branch{grid-template-columns:1fr}}
</style></head><body><div class="wrap">
<div class="top"><div class="title">Nivel 5 · Autofagia durante la infección</div><div class="score">Puntaje: <span id="score">0</span>/800</div></div>
<div class="instructions"><b>Misión:</b> reconstruye cómo una célula puede secuestrar material intracelular o un microorganismo en una vacuola de doble membrana y dirigirlo a degradación lisosomal.</div>
<div class="layout">
<div class="panel"><h3>🧩 Piezas</h3><div id="piecebox"></div></div>
<div class="panel"><div class="cell"><div class="cyto">
<div class="zone">Citoplasma de una célula infectada</div>
<div class="row"><div class="slot" data-answer="Patógeno intracelular">🦠 Blanco intracelular</div></div><div class="arrow">↓</div>
<div class="row"><div class="slot" data-answer="ATG / Beclin">Maquinaria reguladora</div></div><div class="arrow">↓</div>
<div class="row"><div class="slot" data-answer="Fagóforo">Membrana de aislamiento</div></div><div class="arrow">↓ elongación y cierre</div>
<div class="row"><div class="slot" data-answer="ATG8 / LC3">Proteína asociada a la membrana autofágica</div></div><div class="arrow">↓</div>
<div class="row"><div class="slot" data-answer="Autofagosoma">Vacuola de doble membrana</div></div><div class="arrow">+</div>
<div class="row"><div class="slot" data-answer="Lisosoma">Compartimento con enzimas degradativas</div></div><div class="arrow">↓ fusión</div>
<div class="row"><div class="slot" data-answer="Autofagolisosoma">Compartimento de degradación</div></div><div class="arrow">↓</div>
<div class="row"><div class="slot" data-answer="Degradación del contenido">♻️ Degradación</div></div>
</div></div>

<div class="feedback" id="feedback"><b>Retroalimentación</b><br><span class="hint">Identifica primero qué debe ser capturado y qué maquinaria organiza el proceso.</span></div>
<button class="primary" onclick="checkLevel()">Comprobar nivel</button><button class="secondary" onclick="location.reload()">Reiniciar</button>

<div class="question" id="challenge" style="display:none"><b>Desafío: ¿la autofagia siempre beneficia al hospedero?</b>
<button class="option" onclick="answer(this,'no')">No. Puede eliminar patógenos, pero algunos microorganismos pueden subvertir la maquinaria autofágica.</button>
<button class="option" onclick="answer(this,'si')">Sí. Siempre destruye al microorganismo.</button>
<button class="option" onclick="answer(this,'muerte')">Sí. Autofagia significa necesariamente muerte celular.</button>
<div id="cf"></div></div>

<div class="question" id="cases" style="display:none"><b>Reto infeccioso</b><br><br>
<b>1.</b> En una célula infectada por <i>Streptococcus</i> del grupo A, la autofagia puede contribuir principalmente a:
<button class="option" onclick="caseAnswer(this,true,'c1')">Eliminación del patógeno</button>
<button class="option" onclick="caseAnswer(this,false,'c1')">Favorecer obligatoriamente su replicación</button><div id="c1"></div><br>
<b>2.</b> Poliovirus y rinovirus pueden:
<button class="option" onclick="caseAnswer(this,true,'c2')">Subvertir la formación de autofagosomas en beneficio de su replicación</button>
<button class="option" onclick="caseAnswer(this,false,'c2')">Ser siempre destruidos por autofagia</button><div id="c2"></div>
</div>

<div class="summary"><b>Idea clave:</b> autofagia no equivale automáticamente a muerte celular. El material base la describe como un proceso regulado importante para homeostasis y supervivencia; cuando es excesiva puede asociarse con muerte celular autofágica. Durante infección puede ser protectora o ser explotada por determinados patógenos.</div>
</div></div></div>

<script>
const pieces=[
{name:"Patógeno intracelular",info:"Durante la infección, la autofagia puede dirigir microorganismos intracelulares hacia compartimentos degradativos sin eliminar necesariamente toda la célula."},
{name:"ATG / Beclin",info:"El artículo base describe la autofagia como un proceso regulado por proteínas ATG/Beclin."},
{name:"Fagóforo",info:"La membrana de aislamiento comienza a rodear el material que será secuestrado."},
{name:"ATG8 / LC3",info:"ATG8/LC3 se asocia con la membrana autofágica; la figura del material lo representa en la formación del autofagosoma."},
{name:"Autofagosoma",info:"Es una vacuola de doble membrana que captura componentes intracelulares."},
{name:"Lisosoma",info:"Aporta el compartimento y las enzimas necesarias para la degradación lisosomal."},
{name:"Autofagolisosoma",info:"La fusión del autofagosoma con el compartimento lisosomal permite la degradación del contenido secuestrado."},
{name:"Degradación del contenido",info:"El contenido capturado es degradado. Durante infección esto puede contribuir a la eliminación de determinados patógenos."}
];
let score=0,used=new Set();
function shuffle(a){return [...a].sort(()=>Math.random()-0.5)}
function render(){const box=document.getElementById("piecebox");shuffle(pieces).forEach(p=>{const e=document.createElement("div");e.className="piece";e.draggable=true;e.textContent=p.name;e.dataset.name=p.name;e.addEventListener("dragstart",x=>x.dataTransfer.setData("text/plain",p.name));box.appendChild(e)})}
document.querySelectorAll(".slot[data-answer]").forEach(s=>{s.addEventListener("dragover",e=>e.preventDefault());s.addEventListener("drop",e=>{e.preventDefault();const n=e.dataTransfer.getData("text/plain"),p=pieces.find(x=>x.name===n);if(!p)return;if(s.dataset.answer===n){if(!used.has(n)){score+=100;used.add(n)}s.className="slot correct";s.innerHTML="<b>"+n+"</b>";const o=[...document.querySelectorAll(".piece")].find(x=>x.dataset.name===n);if(o)o.remove();document.getElementById("score").textContent=score;document.getElementById("feedback").innerHTML='<span class="success">✓ Correcto.</span><br>'+p.info}else{s.classList.add("wrong");setTimeout(()=>s.classList.remove("wrong"),700);document.getElementById("feedback").innerHTML='<span class="error">✗ Incorrecto.</span><br><span class="hint">Piensa en la secuencia: reconocimiento/captura → doble membrana → fusión lisosomal → degradación.</span>'}})})
function checkLevel(){if(used.size===pieces.length){document.getElementById("feedback").innerHTML='<span class="success">🏆 Nivel completado.</span><br>Has reconstruido la secuencia general de autofagia.';document.getElementById("challenge").style.display="block";document.getElementById("cases").style.display="block"}else document.getElementById("feedback").innerHTML='<span class="hint">Aún faltan '+(pieces.length-used.size)+' piezas.</span>'}
function answer(b,a){document.querySelectorAll("#challenge .option").forEach(x=>x.classList.remove("good","bad"));if(a==="no"){b.classList.add("good");document.getElementById("cf").innerHTML='<span class="success">✓ Correcto.</span> El resultado depende del patógeno y del contexto de infección.'}else{b.classList.add("bad");document.getElementById("cf").innerHTML='<span class="error">✗ Incorrecto.</span> Autofagia puede favorecer la defensa, pero no siempre.'}}
function caseAnswer(b,ok,id){if(ok){b.classList.add("good");document.getElementById(id).innerHTML='<span class="success">✓ Correcto.</span>'}else{b.classList.add("bad");document.getElementById(id).innerHTML='<span class="error">✗ Revisa el papel de la autofagia en este patógeno.</span>'}}
render();
</script></body></html>
"""
    components.html(html, height=1800, scrolling=True)

elif nivel == "Nivel 6 · Compara las respuestas celulares":
    html = r"""
<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<style>
*{box-sizing:border-box}body{margin:0;font-family:Arial;background:#f6f8fb;color:#17212b}.wrap{padding:16px}
.top{display:flex;justify-content:space-between;align-items:center;gap:12px}.title{font-size:24px;font-weight:800}
.score{background:#fff;border:1px solid #ddd;border-radius:12px;padding:10px 14px;font-weight:800}
.instructions{background:#f3f0ff;border-left:5px solid #7950f2;padding:12px 14px;border-radius:12px;margin:14px 0}
.layout{display:grid;grid-template-columns:300px 1fr;gap:16px}.panel{background:#fff;border:1px solid #d9dee5;border-radius:16px;padding:16px}
.piece{border:2px solid #7950f2;background:#f3f0ff;border-radius:12px;padding:9px;margin:7px 0;font-weight:750;text-align:center;cursor:grab}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.col{border:1px solid #d5dce3;border-radius:16px;padding:12px;min-height:540px}
.col h3{text-align:center;margin-top:0}.apop{background:#eef6ff}.pyro{background:#fff4e6}.onco{background:#fff0f3}.auto{background:#eefbf5}
.slot{min-height:64px;border:2px dashed #98a5b3;border-radius:12px;background:#ffffffd9;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px;margin:8px 0;font-weight:700}
.correct{border:2px solid #2f9e44!important;background:#e9f8ec!important}.wrong{border:2px solid #d9485f!important;background:#fff0f2!important}
.feedback,.question,.summary{margin-top:14px;padding:14px;border-radius:12px;border:1px solid #d9dee5;background:#fff}
.success{color:#237a35;font-weight:800}.error{color:#c92a2a;font-weight:800}.hint{color:#4d5964}
button{border:0;border-radius:10px;padding:10px 14px;font-weight:800;cursor:pointer;margin-top:10px;margin-right:8px}.primary{background:#263b5e;color:#fff}.secondary{background:#6c757d;color:#fff}
.option{display:block;width:100%;text-align:left;background:#f3f6f9;color:#17212b}.good{background:#e9f8ec!important}.bad{background:#fff0f2!important}
@media(max-width:1100px){.layout{grid-template-columns:1fr}.grid{grid-template-columns:1fr 1fr}}@media(max-width:700px){.grid{grid-template-columns:1fr}}
</style></head><body><div class="wrap">
<div class="top"><div class="title">Nivel 6 · ¿Qué respuesta celular estoy observando?</div><div class="score">Puntaje: <span id="score">0</span>/1600</div></div>
<div class="instructions"><b>Misión integradora:</b> arrastra cada característica al proceso correcto. Algunas características pueden parecer similares: usa el mecanismo, la morfología y el carácter inflamatorio para decidir.</div>
<div class="layout">
<div class="panel"><h3>🧩 Características</h3><div id="piecebox"></div></div>
<div class="panel">
<div class="grid">
<div class="col apop"><h3>🔵 Apoptosis</h3>
<div class="slot" data-answer="Caspasa-3 / -7">Caspasas características</div>
<div class="slot" data-answer="Contracción celular">Cambio de volumen</div>
<div class="slot" data-answer="Cuerpos apoptóticos">Destino morfológico</div>
<div class="slot" data-answer="Poca inflamación">Respuesta inflamatoria</div>
</div>
<div class="col pyro"><h3>🟠 Piroptosis</h3>
<div class="slot" data-answer="Caspasa-1">Caspasa característica</div>
<div class="slot" data-answer="Citocinas maduras">Mediadores</div>
<div class="slot" data-answer="Ruptura de membrana">Membrana</div>
<div class="slot" data-answer="Alta inflamación">Respuesta inflamatoria</div>
</div>
<div class="col onco"><h3>🔴 Oncosis</h3>
<div class="slot" data-answer="Independiente de caspasas">Dependencia de caspasas</div>
<div class="slot" data-answer="Tumefacción celular y de organelos">Morfología</div>
<div class="slot" data-answer="Aumento de permeabilidad">Membrana</div>
<div class="slot" data-answer="Favorece diseminación">Consecuencia descrita</div>
</div>
<div class="col auto"><h3>🟢 Autofagia</h3>
<div class="slot" data-answer="ATG8 / LC3">Marcador del esquema</div>
<div class="slot" data-answer="Autofagosoma">Estructura</div>
<div class="slot" data-answer="Autofagolisosoma">Compartimento final</div>
<div class="slot" data-answer="Poca inflamación">Respuesta inflamatoria</div>
</div>
</div>
<div class="feedback" id="feedback"><b>Retroalimentación</b><br><span class="hint">No te guíes solo por fragmentación del ADN: el material advierte que puede aparecer en más de una modalidad.</span></div>
<button class="primary" onclick="checkLevel()">Comprobar nivel</button><button class="secondary" onclick="location.reload()">Reiniciar</button>
<div class="question" id="challenge" style="display:none"><b>Desafío crítico</b><br>Una célula infectada presenta fragmentación del ADN y condensación nuclear. ¿Es suficiente para concluir que está en apoptosis?
<button class="option" onclick="answer(this,'no')">No. Deben evaluarse eventos más específicos, como liberación de citocromo c o activación de caspasas apoptóticas.</button>
<button class="option" onclick="answer(this,'si')">Sí. Fragmentación de ADN demuestra apoptosis.</button>
<div id="cf"></div></div>
<div class="summary"><b>Idea clave:</b> el artículo compara cuatro respuestas: apoptosis, piroptosis, oncosis y autofagia. Algunas comparten características. Apoptosis y autofagia se presentan como no inflamatorias, mientras piroptosis y oncosis son altamente inflamatorias por liberación de citocinas o contenido citoplasmático.</div>
</div></div></div>
<script>
const pieces=[
{name:"Caspasa-3 / -7",info:"El esquema asocia las caspasas ejecutoras 3 y 7 con apoptosis."},
{name:"Contracción celular",info:"La contracción celular es una característica morfológica de apoptosis."},
{name:"Cuerpos apoptóticos",info:"Durante apoptosis se forman cuerpos apoptóticos que pueden ser eliminados por fagocitos."},
{name:"Poca inflamación",info:"En el esquema, apoptosis y autofagia no inducen la inflamación intensa característica de piroptosis/oncosis.",multi:true},
{name:"Caspasa-1",info:"El artículo vincula piroptosis con activación de caspasa-1."},
{name:"Citocinas maduras",info:"Piroptosis se asocia con maduración/liberación de citocinas inflamatorias."},
{name:"Ruptura de membrana",info:"La ruptura de membrana contribuye a la naturaleza inflamatoria de piroptosis."},
{name:"Alta inflamación",info:"Piroptosis es altamente inflamatoria por liberación de citocinas y contenido celular."},
{name:"Independiente de caspasas",info:"El artículo define oncosis como una muerte independiente de caspasas."},
{name:"Tumefacción celular y de organelos",info:"La oncosis presenta swelling celular y de organelos."},
{name:"Aumento de permeabilidad",info:"La oncosis se caracteriza por aumento de permeabilidad y ruptura de membrana."},
{name:"Favorece diseminación",info:"La figura señala que, en general, la oncosis favorece la diseminación del patógeno."},
{name:"ATG8 / LC3",info:"ATG8/LC3 aparece asociado a las membranas autofágicas en el esquema."},
{name:"Autofagosoma",info:"La autofagia secuestra material en un autofagosoma de doble membrana."},
{name:"Autofagolisosoma",info:"El autofagosoma se fusiona con el compartimento lisosomal para degradar su contenido."}
];
let score=0,placed=0;
function shuffle(a){return [...a].sort(()=>Math.random()-0.5)}
function render(){const b=document.getElementById("piecebox");let arr=[...pieces,{name:"Poca inflamación",info:"En el esquema, apoptosis y autofagia no inducen inflamación intensa."}];shuffle(arr).forEach((p,i)=>{const e=document.createElement("div");e.className="piece";e.draggable=true;e.textContent=p.name;e.dataset.id=i;e.dataset.name=p.name;e.addEventListener("dragstart",x=>{x.dataTransfer.setData("text/plain",JSON.stringify({name:p.name,id:i}))});b.appendChild(e)})}
document.querySelectorAll(".slot").forEach(s=>{s.addEventListener("dragover",e=>e.preventDefault());s.addEventListener("drop",e=>{e.preventDefault();let d;try{d=JSON.parse(e.dataTransfer.getData("text/plain"))}catch{return}const p=pieces.find(x=>x.name===d.name);if(s.dataset.answer===d.name&&!s.classList.contains("correct")){score+=100;placed++;s.classList.add("correct");s.innerHTML="<b>"+d.name+"</b>";const o=[...document.querySelectorAll(".piece")].find(x=>x.dataset.id==d.id);if(o)o.remove();document.getElementById("score").textContent=score;document.getElementById("feedback").innerHTML='<span class="success">✓ Correcto.</span><br>'+(p?p.info:"Clasificación correcta.")}else{s.classList.add("wrong");setTimeout(()=>s.classList.remove("wrong"),650);document.getElementById("feedback").innerHTML='<span class="error">✗ Incorrecto.</span><br><span class="hint">Compara caspasas, membrana, morfología e inflamación.</span>'}})})
function checkLevel(){if(placed===16){document.getElementById("feedback").innerHTML='<span class="success">🏆 Nivel completado.</span><br>Has diferenciado las cuatro respuestas celulares del esquema.';document.getElementById("challenge").style.display="block"}else document.getElementById("feedback").innerHTML='<span class="hint">Aún faltan '+(16-placed)+' características.</span>'}
function answer(b,a){if(a==="no"){b.classList.add("good");document.getElementById("cf").innerHTML='<span class="success">✓ Correcto.</span> El artículo advierte que TUNEL/fragmentación de ADN no es específico de apoptosis.'}else{b.classList.add("bad");document.getElementById("cf").innerHTML='<span class="error">✗ Incorrecto.</span> Otras formas de muerte también pueden presentar fragmentación de ADN.'}}
render();
</script></body></html>
"""
    components.html(html, height=1450, scrolling=True)

elif nivel == "Nivel 7 · Patógeno → respuesta celular":
    html = r"""
<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<style>
*{box-sizing:border-box}body{margin:0;font-family:Arial;background:#f6f8fb;color:#17212b}.wrap{padding:16px}
.top{display:flex;justify-content:space-between;align-items:center;gap:12px}.title{font-size:24px;font-weight:800}
.score{background:#fff;border:1px solid #ddd;border-radius:12px;padding:10px 14px;font-weight:800}
.instructions{background:#eef5ff;border-left:5px solid #2563eb;padding:12px 14px;border-radius:12px;margin:14px 0}
.note{background:#fff8e6;border-left:5px solid #f59f00;padding:11px 14px;border-radius:12px;margin-bottom:14px}
.layout{display:grid;grid-template-columns:350px 1fr;gap:16px}.panel{background:#fff;border:1px solid #d9dee5;border-radius:16px;padding:16px}
.card{border:2px solid #64748b;background:#f8fafc;border-radius:12px;padding:10px;margin:8px 0;font-weight:800;text-align:center;cursor:grab}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.col{border:1px solid #d5dce3;border-radius:16px;padding:12px;min-height:570px}
.col h3{text-align:center;margin-top:0}.apop{background:#eef6ff}.pyro{background:#fff4e6}.onco{background:#fff0f3}.auto{background:#eefbf5}
.slot{min-height:72px;border:2px dashed #98a5b3;border-radius:12px;background:#ffffffd9;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px;margin:8px 0;font-weight:700}
.correct{border:2px solid #2f9e44!important;background:#e9f8ec!important}.wrong{border:2px solid #d9485f!important;background:#fff0f2!important}
.feedback,.question,.summary{margin-top:14px;padding:14px;border-radius:12px;border:1px solid #d9dee5;background:#fff}
.success{color:#237a35;font-weight:800}.error{color:#c92a2a;font-weight:800}.hint{color:#4d5964}
button{border:0;border-radius:10px;padding:10px 14px;font-weight:800;cursor:pointer;margin-top:9px;margin-right:7px}.primary{background:#263b5e;color:#fff}.secondary{background:#6c757d;color:#fff}
.option{display:block;width:100%;text-align:left;background:#f3f6f9;color:#17212b}.good{background:#e9f8ec!important}.bad{background:#fff0f2!important}
.badge{font-size:12px;font-weight:800;border-radius:999px;padding:3px 8px;background:#e2e8f0;display:inline-block;margin-top:4px}
@media(max-width:1100px){.layout{grid-template-columns:1fr}.grid{grid-template-columns:1fr 1fr}}@media(max-width:700px){.grid{grid-template-columns:1fr}}
</style></head><body><div class="wrap">

<div class="top">
  <div class="title">Nivel 7 · Patógeno → respuesta celular</div>
  <div class="score">Puntaje: <span id="score">0</span>/1600</div>
</div>

<div class="instructions">
  <b>Misión final:</b> clasifica 16 escenarios infecciosos. Hay <b>4 escenarios por cada desenlace</b>.
  El orden dentro de cada columna no importa.
</div>

<div class="note">
  <b>Precisión científica:</b> la cuarta columna roja se denomina
  <b>“Oncosis / muerte lítica caspasa-independiente”</b> porque el artículo no documenta
  cuatro microorganismos diferentes como oncosis clásica. Incluye fenómenos caspasa-independientes
  u oncóticos relacionados, claramente identificados por su contexto experimental.
</div>

<div class="layout">
<div class="panel"><h3>🦠 Escenarios infecciosos</h3><div id="piecebox"></div></div>
<div class="panel">
<div class="grid">

<div class="col apop"><h3>🔵 Apoptosis</h3>
<div class="slot" data-category="apoptosis"></div>
<div class="slot" data-category="apoptosis"></div>
<div class="slot" data-category="apoptosis"></div>
<div class="slot" data-category="apoptosis"></div>
</div>

<div class="col pyro"><h3>🟠 Piroptosis</h3>
<div class="slot" data-category="piroptosis"></div>
<div class="slot" data-category="piroptosis"></div>
<div class="slot" data-category="piroptosis"></div>
<div class="slot" data-category="piroptosis"></div>
</div>

<div class="col onco"><h3>🔴 Oncosis / muerte lítica caspasa-independiente</h3>
<div class="slot" data-category="oncosis"></div>
<div class="slot" data-category="oncosis"></div>
<div class="slot" data-category="oncosis"></div>
<div class="slot" data-category="oncosis"></div>
</div>

<div class="col auto"><h3>🟢 Autofagia</h3>
<div class="slot" data-category="autofagia"></div>
<div class="slot" data-category="autofagia"></div>
<div class="slot" data-category="autofagia"></div>
<div class="slot" data-category="autofagia"></div>
</div>

</div>

<div class="feedback" id="feedback">
<b>Retroalimentación</b><br>
<span class="hint">Clasifica por la modalidad documentada para ese contexto; un mismo patógeno puede activar más de una respuesta.</span>
</div>

<button class="primary" onclick="checkLevel()">Comprobar nivel</button>
<button class="secondary" onclick="location.reload()">Reiniciar</button>

<div class="question" id="challenge" style="display:none">
<b>Desafío final</b><br>
¿Por qué un mismo patógeno puede aparecer en más de una columna?
<button class="option" onclick="answer(this,'contexto')">Porque el tipo de respuesta depende de la célula infectada, la carga, los factores de virulencia y las vías activadas o inhibidas.</button>
<button class="option" onclick="answer(this,'taxonomia')">Porque la tinción de Gram determina directamente la modalidad de muerte.</button>
<button class="option" onclick="answer(this,'unica')">No debería aparecer; cada microorganismo induce una única modalidad.</button>
<div id="cf"></div>
</div>

<div class="summary">
<b>Mensaje integrador:</b> la asociación se refiere al <b>escenario experimental descrito</b>, no a una propiedad taxonómica fija del microorganismo.
</div>
</div></div></div>

<script>
const cards=[
// APOPTOSIS
{name:"S. pneumoniae",label:"🟣 Gram (+) · Streptococcus pneumoniae",category:"apoptosis",info:"Apoptosis de macrófagos alveolares; en el artículo se asocia con eliminación del patógeno."},
{name:"H. pylori",label:"🔴 Gram (−) · Helicobacter pylori",category:"apoptosis",info:"El artículo describe apoptosis de células epiteliales gástricas dependiente de Fas."},
{name:"P. aeruginosa · apoptosis",label:"🔴 Gram (−) · Pseudomonas aeruginosa",category:"apoptosis",info:"En ratones WT, la infección produjo apoptosis de células epiteliales pulmonares; la señalización CD95 participa en la defensa."},
{name:"Yersinia · apoptosis",label:"🔴 Gram (−) · Yersinia pseudotuberculosis / Y. pestis",category:"apoptosis",info:"En macrófagos, YopJ inhibe NF-κB/MAPK y se asocia con apoptosis y supervivencia del patógeno."},

// PIROPTOSIS
{name:"Shigella",label:"🔴 Gram (−) · Shigella flexneri",category:"piroptosis",info:"Muerte de macrófagos dependiente de caspasa-1; el artículo la diferencia de apoptosis."},
{name:"Salmonella",label:"🔴 Gram (−) · Salmonella Typhimurium",category:"piroptosis",info:"En macrófagos se describe muerte rápida dependiente de caspasa-1."},
{name:"Listeria",label:"🟣 Gram (+) · Listeria monocytogenes",category:"piroptosis",info:"El artículo incluye piroptosis asociada a reconocimiento por inflamasoma y aclaramiento."},
{name:"Francisella",label:"🔴 Gram (−) · Francisella tularensis",category:"piroptosis",info:"Macrófagos deficientes en caspasa-1/ASC son resistentes a la muerte rápida; el desenlace se relaciona con aclaramiento."},

// ONCOSIS / CASPASE-INDEPENDENT
{name:"MTB alta carga",label:"🟤 Micobacteria · M. tuberculosis (alta MOI)",category:"oncosis",info:"A alta carga intracelular, el artículo describe muerte caspasa-independiente."},
{name:"Shigella alta MOI",label:"🔴 Gram (−) · Shigella flexneri (alta MOI)",category:"oncosis",info:"A mayor MOI se describe pyronecrosis, una muerte caspasa-1-independiente."},
{name:"Pseudomonas ExoU",label:"🔴 Gram (−) · P. aeruginosa ExoU+",category:"oncosis",info:"Cepas ExoU+ bloquean caspasa-1 pero matan eficientemente macrófagos mediante muerte caspasa-independiente."},
{name:"B. pseudomallei",label:"🔴 Gram (−) · Burkholderia pseudomallei",category:"oncosis",info:"El artículo señala un fenotipo oncótico en células infectadas, aunque lo clasifica experimentalmente dentro de muerte dependiente de caspasa-1. Se incluye aquí como ejemplo morfológico oncótico."},

// AUTOPHAGY
{name:"MTB autofagia",label:"🟤 Micobacteria · Mycobacterium tuberculosis",category:"autofagia",info:"La autofagia puede superar el bloqueo de maduración fagolisosomal y favorecer degradación bacteriana."},
{name:"Listeria autofagia",label:"🟣 Gram (+) · Listeria monocytogenes",category:"autofagia",info:"El artículo describe a Listeria como blanco de autofagia y la relaciona con aclaramiento."},
{name:"Salmonella autofagia",label:"🔴 Gram (−) · Salmonella enterica",category:"autofagia",info:"La autofagia puede controlar Salmonella tras daño de la vacuola que contiene la bacteria."},
{name:"Toxoplasma",label:"🦠 Parásito · Toxoplasma gondii",category:"autofagia",info:"El artículo incluye T. gondii entre los patógenos dirigidos a eliminación por autofagia."}
];

let score=0,placed=0,dragged=null;
function shuffle(a){return [...a].sort(()=>Math.random()-0.5)}

function render(){
 const b=document.getElementById("piecebox");
 shuffle(cards).forEach(p=>{
   const e=document.createElement("div");
   e.className="card"; e.draggable=true;
   e.innerHTML=p.label+'<br><span class="badge">arrastra según el contexto</span>';
   e.addEventListener("dragstart",ev=>{
      dragged={...p,element:e};
      ev.dataTransfer.setData("text/plain",p.name);
   });
   b.appendChild(e);
 });
}

document.querySelectorAll(".slot").forEach(s=>{
 s.addEventListener("dragover",e=>e.preventDefault());
 s.addEventListener("drop",e=>{
   e.preventDefault();
   if(!dragged || s.classList.contains("correct"))return;
   if(s.dataset.category===dragged.category){
     score+=100; placed++;
     s.classList.add("correct");
     s.innerHTML="<b>"+dragged.label+"</b>";
     dragged.element.remove();
     document.getElementById("score").textContent=score;
     document.getElementById("feedback").innerHTML='<span class="success">✓ Correcto.</span><br>'+dragged.info;
   }else{
     s.classList.add("wrong");setTimeout(()=>s.classList.remove("wrong"),650);
     document.getElementById("feedback").innerHTML='<span class="error">✗ No corresponde a esa modalidad.</span><br><span class="hint">Usa el contexto experimental, no solo el tipo de microorganismo.</span>';
   }
   dragged=null;
 });
});

function checkLevel(){
 if(placed===16){
   document.getElementById("feedback").innerHTML='<span class="success">🏆 Nivel completado.</span><br>Clasificaste los 16 escenarios.';
   document.getElementById("challenge").style.display="block";
 }else{
   document.getElementById("feedback").innerHTML='<span class="hint">Aún faltan '+(16-placed)+' escenarios.</span>';
 }
}

function answer(b,a){
 if(a==="contexto"){
  b.classList.add("good");
  document.getElementById("cf").innerHTML='<span class="success">✓ Correcto.</span> Esa es la idea central de la actividad.';
 }else{
  b.classList.add("bad");
  document.getElementById("cf").innerHTML='<span class="error">✗ Incorrecto.</span> La modalidad no está determinada únicamente por la taxonomía.';
 }
}
render();
</script></body></html>
"""
    components.html(html, height=1850, scrolling=True)
