
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Muerte celular en la infección", page_icon="🧬", layout="wide")
st.title("🧬 Muerte celular en la infección")
st.caption("Puzzle interactivo · Nivel 1: apoptosis extrínseca")

html = r'''
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
body{font-family:Arial;margin:0;background:#f7f9fb;color:#15202b}
.wrap{padding:18px}
.header{display:flex;justify-content:space-between;align-items:center}
.title{font-size:24px;font-weight:700}
.score{background:#fff;border:1px solid #d7dde3;border-radius:12px;padding:10px 14px;font-weight:700}
.instructions{background:#eef5ff;border-left:5px solid #4c7bd9;padding:12px 14px;border-radius:10px;margin:16px 0}
.board{display:grid;grid-template-columns:1fr 2.3fr;gap:16px}
.pieces,.pathway{background:#fff;border:1px solid #d8dee5;border-radius:16px;padding:16px}
.piece{background:#fff7e6;border:2px solid #e7a83b;border-radius:12px;padding:10px;margin:8px 0;cursor:grab;font-weight:700;text-align:center}
.slots{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.slot{min-height:92px;border:2px dashed #9aa7b4;border-radius:14px;background:#f9fbfd;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px}
.slot.correct{border:2px solid #2f9e44;background:#ebfbee}
.slot.wrong{border:2px solid #e03131;background:#fff5f5}
.arrow{text-align:center;font-size:26px;padding:6px}
.feedback{margin-top:16px;padding:14px;border-radius:12px;border:1px solid #d8dee5;background:#fff;min-height:82px}
.success{color:#237a35;font-weight:700}.error{color:#c92a2a;font-weight:700}.hint{color:#495057}
button{border:0;border-radius:10px;padding:10px 14px;font-weight:700;cursor:pointer;background:#263b5e;color:white;margin-top:12px;margin-right:8px}
.secondary{background:#6c757d}
@media(max-width:900px){.board{grid-template-columns:1fr}.slots{grid-template-columns:1fr 1fr}}
</style>
</head>
<body>
<div class="wrap">
<div class="header"><div class="title">Nivel 1 · Vía extrínseca</div><div class="score">Puntaje: <span id="score">0</span>/800</div></div>
<div class="instructions">Arrastra cada pieza a la posición correcta. Cada acierto vale 100 puntos.</div>
<div class="board">
<div class="pieces"><h3>🧩 Piezas</h3><div id="piecebox"></div></div>
<div class="pathway">
<h3>🧬 Construye la señal</h3>
<div class="slots">
<div class="slot" data-answer="Ligando de muerte">1. Señal extracelular</div>
<div class="slot" data-answer="Receptor de muerte">2. Membrana plasmática</div>
<div class="slot" data-answer="FADD / TRADD">3. Adaptadores</div>
<div class="slot" data-answer="DISC">4. Complejo de señalización</div>
</div>
<div class="arrow">↓</div>
<div class="slots">
<div class="slot" data-answer="Procaspasa-8 / -10">5. Procaspasas iniciadoras</div>
<div class="slot" data-answer="Caspasa-8 / -10">6. Caspasas iniciadoras activas</div>
<div class="slot" data-answer="Caspasa-3 / -7">7. Caspasas ejecutoras</div>
<div class="slot" data-answer="Apoptosis">8. Desenlace</div>
</div>
<div class="feedback" id="feedback"><b>Retroalimentación</b><br><span class="hint">Comienza con la señal extracelular.</span></div>
<button onclick="checkLevel()">Comprobar nivel</button>
<button class="secondary" onclick="location.reload()">Reiniciar</button>
</div>
</div>
</div>
<script>
const piecesData=[
{name:"Ligando de muerte",info:"TNF-α, FasL o TRAIL pueden actuar como señales extracelulares de muerte."},
{name:"Receptor de muerte",info:"Receptores como TNFR1 o FAS transmiten la señal desde la membrana."},
{name:"FADD / TRADD",info:"Proteínas adaptadoras que conectan el receptor con la maquinaria de caspasas."},
{name:"DISC",info:"Complejo de señalización que recluta procaspasas iniciadoras."},
{name:"Procaspasa-8 / -10",info:"Formas inactivas de caspasas iniciadoras."},
{name:"Caspasa-8 / -10",info:"Caspasas iniciadoras activas; también pueden conectar con la vía mitocondrial mediante BID."},
{name:"Caspasa-3 / -7",info:"Caspasas ejecutoras responsables de cambios celulares de apoptosis."},
{name:"Apoptosis",info:"Muerte celular programada con contracción celular, condensación de cromatina y cuerpos apoptóticos."}
];
let score=0,used=new Set();
function shuffle(a){return [...a].sort(()=>Math.random()-0.5)}
function render(){
 const box=document.getElementById("piecebox");
 shuffle(piecesData).forEach(p=>{
  const el=document.createElement("div"); el.className="piece"; el.draggable=true; el.textContent=p.name; el.dataset.name=p.name;
  el.addEventListener("dragstart",e=>e.dataTransfer.setData("text/plain",p.name)); box.appendChild(el);
 });
}
document.querySelectorAll(".slot").forEach(slot=>{
 slot.addEventListener("dragover",e=>e.preventDefault());
 slot.addEventListener("drop",e=>{
  e.preventDefault(); const name=e.dataTransfer.getData("text/plain"); const piece=piecesData.find(x=>x.name===name);
  if(slot.dataset.answer===name){
   if(!used.has(name)){score+=100;used.add(name)}
   slot.className="slot correct"; slot.innerHTML="<b>"+name+"</b>";
   const p=[...document.querySelectorAll(".piece")].find(x=>x.dataset.name===name); if(p)p.remove();
   document.getElementById("score").textContent=score;
   document.getElementById("feedback").innerHTML='<span class="success">✓ Correcto.</span><br>'+piece.info;
  }else{
   slot.classList.add("wrong"); setTimeout(()=>slot.classList.remove("wrong"),600);
   document.getElementById("feedback").innerHTML='<span class="error">✗ Incorrecto.</span><br><span class="hint">Piensa qué componente actúa antes y cuál después.</span>';
  }
 });
});
function checkLevel(){
 document.getElementById("feedback").innerHTML=used.size===8
 ?'<span class="success">🏆 Nivel completado.</span><br>Ligando → receptor → adaptadores → DISC → caspasas iniciadoras → caspasas ejecutoras → apoptosis.'
 :'<span class="hint">Aún faltan '+(8-used.size)+' piezas.</span>';
}
render();
</script>
</body>
</html>
'''
components.html(html, height=760, scrolling=True)
