import os
import base64
import subprocess

PROJECT_DIR = "/home/antonio/Documentos/DAM/Acceso-a-Datos/UT4/Examen"
CAPTURES_DIR = os.path.join(PROJECT_DIR, "docs/capturas")
OUTPUT_HTML = os.path.join(PROJECT_DIR, "presentacion.html")
OUTPUT_PDF = os.path.join(PROJECT_DIR, "Presentacion_UT4_Antonio_Cano_Ruiz.pdf")

def get_base64_img(filename):
    path = os.path.join(CAPTURES_DIR, filename)
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/png;base64,{data}"

img_db = get_base64_img("01_script_sql_postgresql.png")
img_model = get_base64_img("06_jerarquia_nave_abstracta.png")
img_subclasses = get_base64_img("07_subclases_polimorficas.png")
img_d1 = get_base64_img("08_desafio1_hql_type.png")
img_d2 = get_base64_img("09_desafio2_hql_fetch_join.png")
img_d3 = get_base64_img("10_desafio3_hql_proyeccion.png")
img_results = get_base64_img("11_ejecucion_main_resultados.png")

template = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Presentación UT4 - Persistencia Polimórfica - Antonio Cano Ruiz</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

  @page {
    size: 297mm 210mm;
    margin: 0;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    background: #090d16;
    color: #f1f5f9;
    font-family: 'Inter', -apple-system, sans-serif;
    overflow-x: hidden;
    user-select: none;
  }

  .deck {
    position: relative;
    width: 100vw;
    height: 100vh;
  }

  .slide {
    display: none;
    width: 100vw;
    height: 100vh;
    padding: 48px 64px;
    background: radial-gradient(circle at 80% 20%, rgba(37, 99, 235, 0.12) 0%, rgba(9, 13, 22, 1) 70%);
    position: relative;
    flex-direction: column;
    justify-content: space-between;
  }

  .slide.active {
    display: flex;
  }

  /* HEADER */
  .slide-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 16px;
  }

  .slide-tag {
    background: rgba(56, 189, 248, 0.15);
    color: #38bdf8;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    border: 1px solid rgba(56, 189, 248, 0.3);
  }

  .slide-meta {
    font-size: 13px;
    color: #94a3b8;
    font-family: 'JetBrains Mono', monospace;
  }

  /* BODY */
  .slide-content {
    flex-grow: 1;
    display: flex;
    gap: 40px;
    align-items: center;
    margin: 24px 0;
  }

  .col-text {
    flex: 1.1;
  }

  .col-visual {
    flex: 1.3;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .col-visual img {
    max-width: 100%;
    max-height: 58vh;
    border-radius: 10px;
    box-shadow: 0 16px 36px rgba(0,0,0,0.7), 0 0 0 1px rgba(255,255,255,0.12);
  }

  h1.title {
    font-size: 36px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 16px;
    letter-spacing: -0.02em;
  }

  h2.subtitle {
    font-size: 19px;
    font-weight: 400;
    color: #94a3b8;
    margin-bottom: 24px;
  }

  .points {
    list-style: none;
    margin: 0;
  }

  .points li {
    margin-bottom: 14px;
    font-size: 16.5px;
    color: #cbd5e1;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    line-height: 1.45;
  }

  .points li .icon {
    color: #38bdf8;
    font-size: 18px;
    margin-top: 1px;
  }

  .points li strong {
    color: #ffffff;
  }

  .code-pill {
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid #334155;
    color: #38bdf8;
    padding: 2px 8px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13.5px;
  }

  .alert-box {
    background: rgba(30, 58, 138, 0.35);
    border-left: 4px solid #38bdf8;
    padding: 12px 16px;
    border-radius: 6px;
    margin-top: 18px;
    font-size: 14px;
    color: #e2e8f0;
  }

  /* FOOTER */
  .slide-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 16px;
    font-size: 13px;
    color: #64748b;
  }

  .author-info {
    font-weight: 600;
    color: #94a3b8;
  }

  /* PORTADA ESPECIAL */
  .cover {
    justify-content: center;
    align-items: center;
    text-align: center;
    background: radial-gradient(circle at center, rgba(37, 99, 235, 0.22) 0%, rgba(9, 13, 22, 1) 75%);
  }

  .cover-card {
    max-width: 860px;
    padding: 48px;
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 24px 60px rgba(0,0,0,0.8);
  }

  .cover-badge {
    display: inline-block;
    background: #2563eb;
    color: #ffffff;
    font-size: 13px;
    font-weight: 700;
    padding: 6px 18px;
    border-radius: 999px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 24px;
  }

  .cover-title {
    font-size: 44px;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.15;
    margin-bottom: 16px;
    letter-spacing: -0.03em;
  }

  .cover-subtitle {
    font-size: 19px;
    color: #94a3b8;
    line-height: 1.5;
    margin-bottom: 32px;
  }

  .cover-meta {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 24px;
    text-align: left;
  }

  .cover-meta-item p {
    font-size: 12px;
    color: #64748b;
    text-transform: uppercase;
    margin-bottom: 4px;
  }

  .cover-meta-item h4 {
    font-size: 16px;
    color: #f8fafc;
    font-weight: 600;
  }

  /* CONTROLES NAVEGACIÓN EN PANTALLA */
  .nav-controls {
    position: fixed;
    bottom: 24px;
    right: 32px;
    display: flex;
    gap: 12px;
    z-index: 100;
  }

  .nav-btn {
    background: rgba(30, 41, 59, 0.85);
    color: #e2e8f0;
    border: 1px solid rgba(255,255,255,0.15);
    width: 42px;
    height: 42px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 18px;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all 0.2s;
  }

  .nav-btn:hover {
    background: #2563eb;
    color: white;
    transform: scale(1.08);
  }

  /* MODAL NOTAS DEL ORADOR */
  #speakerNotes {
    position: fixed;
    bottom: 80px;
    left: 32px;
    max-width: 480px;
    background: rgba(15, 23, 42, 0.95);
    border: 1px solid #38bdf8;
    box-shadow: 0 12px 30px rgba(0,0,0,0.8);
    border-radius: 10px;
    padding: 16px 20px;
    display: none;
    z-index: 200;
    font-size: 13.5px;
    line-height: 1.45;
    color: #cbd5e1;
  }

  #speakerNotes h5 {
    color: #38bdf8;
    margin-bottom: 6px;
    font-size: 13px;
    text-transform: uppercase;
  }

  /* ESTILO PARA IMPRESIÓN PDF */
  @media print {
    body {
      background: #090d16 !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }
    .deck {
      width: 100%;
      height: auto;
    }
    .slide {
      display: flex !important;
      width: 100vw !important;
      height: 100vh !important;
      page-break-after: always !important;
      page-break-inside: avoid !important;
    }
    .nav-controls, #speakerNotes {
      display: none !important;
    }
  }
</style>
</head>
<body>

<div class="deck">

  <!-- SLIDE 1: PORTADA -->
  <div class="slide cover active" data-notes="Presentación formal: Saludar, dar tu nombre (Antonio Cano Ruiz), módulo (Acceso a Datos) y explicar que vamos a resolver el desfase objeto-relacional mediante persistencia polimórfica en Hibernate 6 con la estrategia SINGLE_TABLE y optimización de consultas en HQL.">
    <div class="cover-card">
      <div class="cover-badge">Acceso a Datos (2º DAM) &bull; UT4 - Persistencia</div>
      <h1 class="cover-title">Sistema de Inteligencia Táctica HoloNet</h1>
      <p class="cover-subtitle">Persistencia Polimórfica con Hibernate 6, PostgreSQL y Consultas HQL Avanzadas</p>
      <div class="cover-meta">
        <div class="cover-meta-item">
          <p>Alumno / Desarrollador</p>
          <h4>Antonio Cano Ruiz</h4>
        </div>
        <div class="cover-meta-item">
          <p>Estrategia de Mapeo</p>
          <h4>InheritanceType.SINGLE_TABLE</h4>
        </div>
      </div>
    </div>
  </div>

  <!-- SLIDE 2: CONTEXTO Y DESFASE OBJETO-RELACIONAL -->
  <div class="slide" data-notes="Explicar el Impedance Mismatch: Java entiende clases abstractas y subtipos (Caza, Destructor). PostgreSQL sólo entiende tablas planas y claves ajenas. ¿Cómo representamos la herencia sin penalizar el rendimiento? Eligiendo SINGLE_TABLE.">
    <div class="slide-header">
      <span class="slide-tag">01. Arquitectura &amp; Concepto</span>
      <span class="slide-meta">HoloNet / UT4</span>
    </div>
    <div class="slide-content">
      <div class="col-text">
        <h1 class="title">El Desfase Objeto-Relacional (Impedance Mismatch)</h1>
        <h2 class="subtitle">¿Cómo persistir una jerarquía POO en tablas relacionales?</h2>
        <ul class="points">
          <li><span class="icon">&#9656;</span> <div><strong>El Problema:</strong> Las bases de datos relacionales no soportan herencia nativa de clases (cazas y destructores derivan de <code>Nave</code>).</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>La Solución:</strong> Patrón <code>SINGLE_TABLE</code> (Tabla Única). Todas las entidades hijas conviven en la misma tabla física <code>naves</code>.</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Ventaja Competitiva:</strong> Máxima velocidad de lectura. Cero operaciones <code>JOIN</code> entre tablas jerárquicas y cero <code>UNION</code>.</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Coste de Diseño:</strong> Los campos específicos de cada subclase deben admitir valores <code>NULL</code>.</div></li>
        </ul>
        <div class="alert-box">
          <strong>Clave ORM:</strong> Hibernate utiliza una <strong>columna discriminadora</strong> para instanciar la clase exacta en tiempo de ejecución.
        </div>
      </div>
      <div class="col-visual">
        <img src="IMG_DB" alt="DDL Base de Datos">
      </div>
    </div>
    <div class="slide-footer">
      <span class="author-info">Antonio Cano Ruiz</span>
      <span>2 / 9</span>
    </div>
  </div>

  <!-- SLIDE 3: ESTRUCTURA POSTGRESQL -->
  <div class="slide" data-notes="Mencionar la estructura: tabla planetas (independiente) y tabla naves (polimórfica). Resaltar la columna discriminadora 'tipo_nave' ('CAZA' / 'DESTRUCTOR') y las columnas nulables (potencia_fuego, capacidad_escudos).">
    <div class="slide-header">
      <span class="slide-tag">02. Base de Datos Física</span>
      <span class="slide-meta">PostgreSQL 16</span>
    </div>
    <div class="slide-content">
      <div class="col-text">
        <h1 class="title">Diseño Relacional Desnormalizado</h1>
        <h2 class="subtitle">Estructura física de las tablas <code>planetas</code> y <code>naves</code></h2>
        <ul class="points">
          <li><span class="icon">&#9656;</span> <div><span class="code-pill">tipo_nave VARCHAR(30)</span> Columna discriminadora obligatoria (valores: <code>CAZA</code> o <code>DESTRUCTOR</code>).</div></li>
          <li><span class="icon">&#9656;</span> <div><span class="code-pill">potencia_fuego INT</span> Específico de cazas (<code>NULL</code> para destructores).</div></li>
          <li><span class="icon">&#9656;</span> <div><span class="code-pill">capacidad_escudos INT</span> Específico de destructores (<code>NULL</code> para cazas).</div></li>
          <li><span class="icon">&#9656;</span> <div><span class="code-pill">CONSTRAINT fk_planeta</span> Clave foránea hacia <code>planetas(planeta_id)</code> con <code>ON DELETE SET NULL</code>.</div></li>
        </ul>
        <div class="alert-box">
          Se insertaron 3 planetas y 5 naves cubriendo estados <code>Estable</code>, <code>Critico</code> y <code>Mantenimiento</code> para las pruebas de inteligencia.
        </div>
      </div>
      <div class="col-visual">
        <img src="IMG_MODEL" alt="Modelo Nave.java">
      </div>
    </div>
    <div class="slide-footer">
      <span class="author-info">Antonio Cano Ruiz</span>
      <span>3 / 9</span>
    </div>
  </div>

  <!-- SLIDE 4: MAPEO JPA -->
  <div class="slide" data-notes="Explicar las anotaciones JPA obligatorias: @Inheritance(strategy=SINGLE_TABLE) en la clase Nave abstracta, @DiscriminatorColumn, y las subclases con @DiscriminatorValue. Resaltar la relación @ManyToOne LAZY hacia Planeta.">
    <div class="slide-header">
      <span class="slide-tag">03. Mapeo Objeto-Relacional</span>
      <span class="slide-meta">JPA &bull; Hibernate 6</span>
    </div>
    <div class="slide-content">
      <div class="col-text">
        <h1 class="title">Jerarquía de Clases con JPA</h1>
        <h2 class="subtitle">Anotaciones de persistencia y relaciones controladas</h2>
        <ul class="points">
          <li><span class="icon">&#9656;</span> <div><code>@Inheritance(strategy = SINGLE_TABLE)</code>: Informa a Hibernate que unifique la tabla física.</div></li>
          <li><span class="icon">&#9656;</span> <div><code>@DiscriminatorColumn(name = "tipo_nave")</code>: Define el campo de discriminación.</div></li>
          <li><span class="icon">&#9656;</span> <div><code>@ManyToOne(fetch = FetchType.LAZY)</code>: Carga diferida obligatoria hacia <code>Planeta</code> para optimizar la memoria.</div></li>
          <li><span class="icon">&#9656;</span> <div><code>@DiscriminatorValue("CAZA")</code> y <code>("DESTRUCTOR")</code> en las clases especializadas <code>CazaLigero</code> y <code>DestructorEstelar</code>.</div></li>
        </ul>
      </div>
      <div class="col-visual">
        <img src="IMG_SUBCLASSES" alt="Subclases Java">
      </div>
    </div>
    <div class="slide-footer">
      <span class="author-info">Antonio Cano Ruiz</span>
      <span>4 / 9</span>
    </div>
  </div>

  <!-- SLIDE 5: DESAFÍO 1 - TYPE -->
  <div class="slide" data-notes="Desafío 1: El objetivo es devolver sólo cazas operativos por bando. Explicar el uso de TYPE(n) = CazaLigero en HQL para que el ORM discrimine por tipo de subclase y el filtro de mantenimiento (<> 'Mantenimiento').">
    <div class="slide-header">
      <span class="slide-tag">04. Desafío 1 &bull; HQL Avanzado</span>
      <span class="slide-meta">Discriminación con TYPE()</span>
    </div>
    <div class="slide-content">
      <div class="col-text">
        <h1 class="title">Sensor de Escuadrones Polimórfico</h1>
        <h2 class="subtitle">Filtrado dinámico por tipo y relación de afiliación</h2>
        <ul class="points">
          <li><span class="icon">&#9656;</span> <div><strong>Objetivo:</strong> Recuperar solo instancias de <code>CazaLigero</code> operativas asignadas a un bando determinado.</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Uso de <code>TYPE(n)</code>:</strong> Permite comprobar la clase polimórfica directamente en la consulta HQL (<code>TYPE(n) = CazaLigero</code>).</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Filtro Táctico:</strong> <code>n.estadoSistema &lt;&gt; :estadoMantenimiento</code> excluye naves no operativas (como el Halcón Milenario).</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Navegación:</strong> <code>INNER JOIN n.planetaOrigen p</code> filtra por <code>p.afiliacion = :bando</code>.</div></li>
        </ul>
      </div>
      <div class="col-visual">
        <img src="IMG_D1" alt="Desafío 1 HQL">
      </div>
    </div>
    <div class="slide-footer">
      <span class="author-info">Antonio Cano Ruiz</span>
      <span>5 / 9</span>
    </div>
  </div>

  <!-- SLIDE 6: DESAFÍO 2 - FETCH JOIN ANTI N+1 -->
  <div class="slide" data-notes="Desafío 2: Pregunta clásica de examen: ¿Qué es el problema N+1? Al ser LAZY, recuperar N naves y acceder a nave.getPlanetaOrigen() provocaría 1 query + N queries adicionales. Con INNER JOIN FETCH solucionamos esto en un único viaje a la base de datos.">
    <div class="slide-header">
      <span class="slide-tag">05. Desafío 2 &bull; Optimización</span>
      <span class="slide-meta">Mitigación del Problema N+1</span>
    </div>
    <div class="slide-content">
      <div class="col-text">
        <h1 class="title">Mitigación del Problema N+1</h1>
        <h2 class="subtitle">Carga impaciente bajo demanda con <code>INNER JOIN FETCH</code></h2>
        <ul class="points">
          <li><span class="icon">&#9656;</span> <div><strong>El Problema N+1:</strong> Al tener <code>FetchType.LAZY</code>, acceder al planeta de cada nave crítica dispararía 1 query inicial + N consultas secundarias.</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>La Solución HQL:</strong> <code>INNER JOIN FETCH n.planetaOrigen p</code>.</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Efecto en SQL:</strong> Hibernate genera una <strong>única consulta SQL</strong> con <code>JOIN</code>, poblando ambos objetos en memoria simultáneamente (Single Round-Trip).</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Polimorfismo Real:</strong> Recupera naves tanto destructores como cazas en estado <code>'Critico'</code>.</div></li>
        </ul>
      </div>
      <div class="col-visual">
        <img src="IMG_D2" alt="Desafío 2 HQL">
      </div>
    </div>
    <div class="slide-footer">
      <span class="author-info">Antonio Cano Ruiz</span>
      <span>6 / 9</span>
    </div>
  </div>

  <!-- SLIDE 7: DESAFÍO 3 - PROYECCIONES PLANAS -->
  <div class="slide" data-notes="Desafío 3: En reportes no queremos entidades administradas pesadas en la sesión. Usamos proyecciones escalares List<Object[]>. Y aplicamos LEFT JOIN para que si una nave no tiene planeta de origen, no se pierda el registro y aparezca con valor null.">
    <div class="slide-header">
      <span class="slide-tag">06. Desafío 3 &bull; Proyecciones</span>
      <span class="slide-meta">Reporte Escalar Tabular</span>
    </div>
    <div class="slide-content">
      <div class="col-text">
        <h1 class="title">Proyecciones Planas de Inteligencia</h1>
        <h2 class="subtitle">Optimización de memoria y uso de <code>LEFT JOIN</code></h2>
        <ul class="points">
          <li><span class="icon">&#9656;</span> <div><strong>Retorno <code>List&lt;Object[]&gt;</code>:</strong> Proyecta sólo 3 columnas: <code>n.nombre</code>, <code>TYPE(n)</code> y <code>p.nombre</code>.</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Cero Sobrecarga:</strong> No sobrecarga el contexto de persistencia con el seguimiento de estado (Dirty Checking).</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Preservación con <code>LEFT JOIN</code>:</strong> Si una nave no tuviera asignada base planetaria (<code>NULL</code>), no se descarta del reporte táctico.</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Identidad POO:</strong> <code>TYPE(n)</code> proyecta la clase Java concreta instanciada.</div></li>
        </ul>
      </div>
      <div class="col-visual">
        <img src="IMG_D3" alt="Desafío 3 HQL">
      </div>
    </div>
    <div class="slide-footer">
      <span class="author-info">Antonio Cano Ruiz</span>
      <span>7 / 9</span>
    </div>
  </div>

  <!-- SLIDE 8: RESULTADOS EMPÍRICOS -->
  <div class="slide" data-notes="Mostrar la ejecución del MainHangar. Explicar cómo el Halcón Milenario dio 0 resultados en Neutral por mantenimiento, cómo el TIE Alfa y el Ejecutor salieron en Crítico en una sola query SQL, y cómo el reporte listó las 5 naves con sus clases correspondientes.">
    <div class="slide-header">
      <span class="slide-tag">07. Validación &bull; MainHangar</span>
      <span class="slide-meta">Resultados Empíricos</span>
    </div>
    <div class="slide-content">
      <div class="col-text">
        <h1 class="title">Validación y Salida por Consola</h1>
        <h2 class="subtitle">Auditoría del SQL generado y resultados en tiempo de ejecución</h2>
        <ul class="points">
          <li><span class="icon">&#9656;</span> <div><strong>Prueba 1:</strong> Neutral devuelve 0 cazas (Halcón en mantenimiento correctamente descartado). Imperio y Alianza devuelven sus respectivos cazas.</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Prueba 2:</strong> Recupera Superdestructor Ejecutor y Caza TIE Alfa con sus planetas precargados en 1 sola consulta SQL.</div></li>
          <li><span class="icon">&#9656;</span> <div><strong>Prueba 3:</strong> Reporte general plano con las 5 naves y su clase correspondiente.</div></li>
        </ul>
        <div class="alert-box">
          Gestión de conexiones segura garantizada con el patrón <strong>try-with-resources</strong>.
        </div>
      </div>
      <div class="col-visual">
        <img src="IMG_RESULTS" alt="Resultados Consola">
      </div>
    </div>
    <div class="slide-footer">
      <span class="author-info">Antonio Cano Ruiz</span>
      <span>8 / 9</span>
    </div>
  </div>

  <!-- SLIDE 9: CONCLUSIONES -->
  <div class="slide cover" data-notes="Cierre: Agradecer la atención y destacar que hemos demostrado el uso de herencia en JPA, optimización de consultas en HQL evitando el problema N+1 y proyecciones de alto rendimiento. Preguntar si tienen alguna duda.">
    <div class="cover-card">
      <div class="cover-badge">Conclusiones de la Práctica</div>
      <h1 class="cover-title">Persistencia Eficiente con Hibernate 6</h1>
      <ul class="points" style="text-align: left; margin: 20px 0 28px 0;">
        <li><span class="icon">&#10004;</span> <div><strong>SINGLE_TABLE:</strong> La estrategia más veloz para jerarquías polimórficas de alta lectura.</div></li>
        <li><span class="icon">&#10004;</span> <div><strong>FETCH JOIN:</strong> La solución estándar para eliminar el problema N+1 sin perder los beneficios de LAZY.</div></li>
        <li><span class="icon">&#10004;</span> <div><strong>HQL Avanzado:</strong> Manejo de <code>TYPE()</code> y proyecciones escalares tabulares para optimizar memoria.</div></li>
      </ul>
      <p style="color: #38bdf8; font-size: 22px; font-weight: 700; margin-top: 14px;">¡Muchas Gracias! &iquest;Preguntas?</p>
      <p style="color: #64748b; font-size: 13px; margin-top: 8px;">Antonio Cano Ruiz &bull; 2º DAM &bull; Acceso a Datos</p>
    </div>
  </div>

</div>

<!-- CONTROLES FLOTANTES -->
<div class="nav-controls">
  <button class="nav-btn" id="btnNotes" title="Ver Notas del Orador (Tecla S)">📝</button>
  <button class="nav-btn" id="btnPrev" title="Anterior (Flecha Izquierda)">&#9664;</button>
  <button class="nav-btn" id="btnNext" title="Siguiente (Flecha Derecha / Espacio)">&#9654;</button>
</div>

<!-- VENTANA NOTAS DEL ORADOR -->
<div id="speakerNotes">
  <h5>Guión / Notas del Orador (Slide <span id="noteSlideNum">1</span>)</h5>
  <div id="noteContent">Texto de notas</div>
</div>

<script>
  let currentSlide = 0;
  const slides = document.querySelectorAll('.slide');
  const notesBox = document.getElementById('speakerNotes');
  const noteContent = document.getElementById('noteContent');
  const noteSlideNum = document.getElementById('noteSlideNum');

  function updateSlide(index) {
    slides[currentSlide].classList.remove('active');
    currentSlide = (index + slides.length) % slides.length;
    slides[currentSlide].classList.add('active');
    
    // Actualizar notas
    const note = slides[currentSlide].getAttribute('data-notes') || 'Sin notas.';
    noteContent.textContent = note;
    noteSlideNum.textContent = (currentSlide + 1) + ' / ' + slides.length;
  }

  document.getElementById('btnNext').addEventListener('click', () => updateSlide(currentSlide + 1));
  document.getElementById('btnPrev').addEventListener('click', () => updateSlide(currentSlide - 1));
  document.getElementById('btnNotes').addEventListener('click', () => {
    notesBox.style.display = notesBox.style.display === 'block' ? 'none' : 'block';
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
      updateSlide(currentSlide + 1);
    } else if (e.key === 'ArrowLeft') {
      updateSlide(currentSlide - 1);
    } else if (e.key === 's' || e.key === 'S') {
      notesBox.style.display = notesBox.style.display === 'block' ? 'none' : 'block';
    } else if (e.key === 'f' || e.key === 'F') {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
      } else {
        document.exitFullscreen();
      }
    }
  });

  // Inicializar notas
  updateSlide(0);
</script>

</body>
</html>
"""

html_final = template.replace("IMG_DB", img_db) \
                     .replace("IMG_MODEL", img_model) \
                     .replace("IMG_SUBCLASSES", img_subclasses) \
                     .replace("IMG_D1", img_d1) \
                     .replace("IMG_D2", img_d2) \
                     .replace("IMG_D3", img_d3) \
                     .replace("IMG_RESULTS", img_results)

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_final)

print(f"✔ Presentación HTML generada en: {OUTPUT_HTML}")

# Compilar a PDF apaisado 16:9
cmd = [
    "google-chrome",
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1920,1080",
    "--print-to-pdf-no-header",
    f"--print-to-pdf={OUTPUT_PDF}",
    f"file://{OUTPUT_HTML}"
]
subprocess.run(cmd, check=True)
print(f"✔ Presentación PDF generada en: {OUTPUT_PDF}")
