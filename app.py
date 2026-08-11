import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Muerte celular en la infección", page_icon="🧬", layout="wide")
st.title("🧬 Muerte celular en la infección")
st.caption("Puzzle molecular interactivo · Apoptosis, piroptosis y autofagia")

nivel = st.radio(
    "Selecciona el nivel",
    ["Nivel 1 · Vía extrínseca", "Nivel 2 · Vía intrínseca", "Nivel 3 · Conexión BID–tBID"],
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
