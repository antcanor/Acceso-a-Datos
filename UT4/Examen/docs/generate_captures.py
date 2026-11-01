import os
import subprocess
import html

CAPTURES_DIR = "/home/antonio/Documentos/DAM/Acceso-a-Datos/UT4/Examen/docs/capturas"
os.makedirs(CAPTURES_DIR, exist_ok=True)

def render_html_to_png(html_content, output_png_path, width=1100, height=750):
    tmp_html = output_png_path.replace(".png", ".html")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--window-size={width},{height}",
        f"--screenshot={output_png_path}",
        f"file://{tmp_html}"
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)
    print(f"✔ Generado: {output_png_path}")

def wrap_ide_window(title, filename, code_html, breadcrumbs="org.dam.accesodatos.ut4.examen", status_text="Git: master* | UTF-8 | Java 21/25"):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: #121316;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    padding: 24px;
    display: flex;
    justify-content: center;
    align-items: center;
  }}
  .window {{
    width: 1040px;
    background: #1e1f22;
    border-radius: 10px;
    box-shadow: 0 16px 40px rgba(0,0,0,0.6), 0 0 0 1px rgba(255,255,255,0.08);
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}
  .titlebar {{
    background: #2b2d30;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #1e1f22;
    user-select: none;
  }}
  .dots {{
    display: flex;
    gap: 8px;
    margin-right: 18px;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }}
  .dot.red {{ background: #ff5f56; }}
  .dot.yellow {{ background: #ffbd2e; }}
  .dot.green {{ background: #27c93f; }}
  .win-title {{
    color: #9da5b4;
    font-size: 13px;
    font-weight: 500;
    flex-grow: 1;
    text-align: center;
  }}
  .tab-bar {{
    background: #1e1f22;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #2b2d30;
    padding-left: 12px;
  }}
  .tab {{
    background: #2b2d30;
    color: #dfe1e5;
    padding: 8px 16px;
    font-size: 13px;
    font-family: "JetBrains Mono", "Fira Code", monospace;
    border-top: 2px solid #3574f0;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .tab-icon {{
    color: #f78c6c;
    font-weight: bold;
    font-size: 11px;
  }}
  .breadcrumbs {{
    background: #1e1f22;
    color: #7a7e85;
    font-size: 12px;
    padding: 6px 18px;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    font-family: "JetBrains Mono", monospace;
  }}
  .breadcrumbs span {{ color: #a8adb5; }}
  .editor {{
    padding: 18px 22px;
    color: #abb2bf;
    font-family: "JetBrains Mono", "Cascadia Code", "Fira Code", Menlo, monospace;
    font-size: 13.5px;
    line-height: 1.55;
    overflow-x: auto;
  }}
  pre {{ margin: 0; }}
  .kw {{ color: #cf8e6d; font-weight: 600; }}
  .ann {{ color: #bbb529; font-weight: 500; }}
  .cls {{ color: #56a8f5; }}
  .fn {{ color: #56b6c2; }}
  .str {{ color: #6aab73; }}
  .cm {{ color: #7a7e85; font-style: italic; }}
  .num {{ color: #2aacb8; }}
  .var {{ color: #dfdfe0; }}
  .op {{ color: #bcbec4; }}
  .hl-block {{
    background: rgba(53, 116, 240, 0.14);
    border-left: 3px solid #3574f0;
    padding: 3px 8px;
    border-radius: 2px;
    margin: 2px 0;
    display: inline-block;
    width: 100%;
  }}
  .statusbar {{
    background: #2b2d30;
    color: #7a7e85;
    font-size: 11px;
    padding: 4px 16px;
    display: flex;
    justify-content: space-between;
    border-top: 1px solid rgba(255,255,255,0.05);
  }}
</style>
</head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
    <div class="win-title">{title} - IntelliJ IDEA</div>
  </div>
  <div class="tab-bar">
    <div class="tab"><span class="tab-icon">☕</span> {filename}</div>
  </div>
  <div class="breadcrumbs">{breadcrumbs} &gt; <span>{filename}</span></div>
  <div class="editor">
    {code_html}
  </div>
  <div class="statusbar">
    <div>{status_text}</div>
    <div>UTF-8 | 4 spaces | LF</div>
  </div>
</div>
</body>
</html>"""

def wrap_terminal_window(title, prompt_cmd, output_html, status_info="antonio@starfleet-station:~/Examen", width=1100, height=750):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: #121316;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    padding: 24px;
    display: flex;
    justify-content: center;
    align-items: center;
  }}
  .window {{
    width: {width - 50}px;
    background: #0d1117;
    border-radius: 10px;
    box-shadow: 0 16px 40px rgba(0,0,0,0.65), 0 0 0 1px rgba(255,255,255,0.08);
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}
  .titlebar {{
    background: #161b22;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }}
  .dots {{
    display: flex;
    gap: 8px;
    margin-right: 18px;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }}
  .dot.red {{ background: #ff5f56; }}
  .dot.yellow {{ background: #ffbd2e; }}
  .dot.green {{ background: #27c93f; }}
  .win-title {{
    color: #cbd5e1;
    font-size: 13px;
    font-weight: 500;
    flex-grow: 1;
    text-align: center;
    font-family: "JetBrains Mono", monospace;
  }}
  .term-body {{
    padding: 18px 22px;
    color: #e2e8f0;
    font-family: "JetBrains Mono", "Cascadia Code", "Fira Code", monospace;
    font-size: 13px;
    line-height: 1.5;
  }}
  .cmd-line {{
    margin-bottom: 12px;
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }}
  .prompt {{
    color: #38bdf8;
    font-weight: bold;
  }}
  .cmd {{
    color: #f1f5f9;
    font-weight: 600;
  }}
  .term-output {{
    color: #94a3b8;
  }}
  .t-green {{ color: #4ade80; }}
  .t-cyan {{ color: #38bdf8; }}
  .t-yellow {{ color: #facc15; }}
  .t-purple {{ color: #c084fc; }}
  .t-white {{ color: #ffffff; font-weight: 600; }}
  .t-dim {{ color: #64748b; }}
  .t-red {{ color: #f87171; }}
  .tbl {{
    border-collapse: collapse;
    margin: 10px 0;
    width: 100%;
    font-size: 12.5px;
  }}
  .tbl th {{
    border-bottom: 2px solid #334155;
    padding: 5px 10px;
    text-align: left;
    color: #38bdf8;
  }}
  .tbl td {{
    border-bottom: 1px solid #1e293b;
    padding: 4px 10px;
    color: #e2e8f0;
  }}
</style>
</head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
    <div class="win-title">{title}</div>
  </div>
  <div class="term-body">
    <div class="cmd-line">
      <span class="prompt">{status_info}$</span>
      <span class="cmd">{prompt_cmd}</span>
    </div>
    <div class="term-output">
      {output_html}
    </div>
  </div>
</div>
</body>
</html>"""

# -------------------------------------------------------------
# 1. Script DDL PostgreSQL
# -------------------------------------------------------------
html_ddl = """
<pre>
<span class="t-dim">-- Limpieza preventiva de entidades existentes</span>
<span class="t-purple">DROP TABLE IF EXISTS</span> naves;
<span class="t-purple">DROP TABLE IF EXISTS</span> planetas;

<span class="t-dim">-- Creación de la tabla independiente 'planetas'</span>
<span class="t-purple">CREATE TABLE</span> <span class="t-cyan">planetas</span> (
    planeta_id <span class="t-yellow">SERIAL PRIMARY KEY</span>,
    nombre <span class="t-yellow">VARCHAR(100) NOT NULL UNIQUE</span>,
    clima <span class="t-yellow">VARCHAR(50)</span>,
    afiliacion <span class="t-yellow">VARCHAR(50) DEFAULT</span> <span class="t-green">'Neutral'</span>
);

<span class="t-dim">-- Creación de la tabla polimórfica 'naves' (Estrategia SINGLE_TABLE)</span>
<span class="t-purple">CREATE TABLE</span> <span class="t-cyan">naves</span> (
    nave_id <span class="t-yellow">SERIAL PRIMARY KEY</span>,
    <span class="t-white">tipo_nave VARCHAR(30) NOT NULL</span>,           <span class="t-dim">-- Columna Discriminadora ('CAZA' / 'DESTRUCTOR')</span>
    nombre <span class="t-yellow">VARCHAR(100) NOT NULL</span>,
    modelo <span class="t-yellow">VARCHAR(50) NOT NULL</span>,
    estado_sistema <span class="t-yellow">VARCHAR(20) NOT NULL</span>,      <span class="t-dim">-- 'Critico', 'Estable', 'Mantenimiento'</span>
    planeta_origen_id <span class="t-yellow">INT</span>,
    potencia_fuego <span class="t-yellow">INT</span>,                       <span class="t-dim">-- Específico de CazaLigero (adpite NULL)</span>
    capacidad_escudos <span class="t-yellow">INT</span>,                    <span class="t-dim">-- Específico de DestructorEstelar (admite NULL)</span>
    <span class="t-purple">CONSTRAINT</span> fk_planeta <span class="t-purple">FOREIGN KEY</span> (planeta_origen_id) 
        <span class="t-purple">REFERENCES</span> planetas(planeta_id) <span class="t-purple">ON DELETE SET NULL</span>
);
<span class="t-green">✔ CREATE TABLE planetas OK</span>
<span class="t-green">✔ CREATE TABLE naves OK</span>
</pre>
"""
render_html_to_png(
    wrap_terminal_window("PostgreSQL Console - DDL Desnormalizado de Base de Datos", "psql -U antonio -d hangar_imperio_db -f schema_init.sql", html_ddl),
    os.path.join(CAPTURES_DIR, "01_script_sql_postgresql.png"),
    height=620
)

# -------------------------------------------------------------
# 2. Datos Insertados en PostgreSQL
# -------------------------------------------------------------
html_selects = """
<span class="t-cyan">hangar_imperio_db=#</span> <span class="t-white">SELECT * FROM planetas;</span>
<table class="tbl">
  <tr><th>planeta_id</th><th>nombre</th><th>clima</th><th>afiliacion</th></tr>
  <tr><td>1</td><td>Coruscant</td><td>Templado</td><td>Imperio</td></tr>
  <tr><td>2</td><td>Yavin IV</td><td>Jungla</td><td>Alianza Rebelde</td></tr>
  <tr><td>3</td><td>Tatooine</td><td>Árido</td><td>Neutral</td></tr>
</table>
<span class="t-dim">(3 rows)</span>
<br><br>
<span class="t-cyan">hangar_imperio_db=#</span> <span class="t-white">SELECT nave_id, tipo_nave, nombre, modelo, estado_sistema, planeta_origen_id, potencia_fuego, capacidad_escudos FROM naves;</span>
<table class="tbl">
  <tr><th>nave_id</th><th>tipo_nave</th><th>nombre</th><th>modelo</th><th>estado_sistema</th><th>planeta_id</th><th>potencia_fuego</th><th>capacidad_escudos</th></tr>
  <tr><td>1</td><td><span class="t-green">CAZA</span></td><td>Caza X-Wing</td><td>T-65B</td><td>Estable</td><td>2</td><td>85</td><td><span class="t-dim">NULL</span></td></tr>
  <tr><td>2</td><td><span class="t-purple">DESTRUCTOR</span></td><td>Destructor Estelar</td><td>Clase Imperial I</td><td>Estable</td><td>1</td><td><span class="t-dim">NULL</span></td><td>9500</td></tr>
  <tr><td>3</td><td><span class="t-purple">DESTRUCTOR</span></td><td>Superdestructor Ejecutor</td><td>Clase Ejecutor</td><td>Critico</td><td>1</td><td><span class="t-dim">NULL</span></td><td>45000</td></tr>
  <tr><td>4</td><td><span class="t-green">CAZA</span></td><td>Caza TIE Alfa</td><td>TIE/ln</td><td>Critico</td><td>1</td><td>40</td><td><span class="t-dim">NULL</span></td></tr>
  <tr><td>5</td><td><span class="t-green">CAZA</span></td><td>Halcón Milenario</td><td>YT-1300</td><td>Mantenimiento</td><td>3</td><td>120</td><td><span class="t-dim">NULL</span></td></tr>
</table>
<span class="t-dim">(5 rows)</span>
"""
render_html_to_png(
    wrap_terminal_window("PostgreSQL Query Tool - Verificación de Semillas de Datos", "psql -U antonio -d hangar_imperio_db", html_selects),
    os.path.join(CAPTURES_DIR, "02_datos_insertados_psql.png"),
    height=620
)

# -------------------------------------------------------------
# 3. Dependencias en pom.xml
# -------------------------------------------------------------
html_pom = """
<pre>
    <span class="cm">&lt;!-- Dependencias del Proyecto Maven para Hibernate 6 y PostgreSQL --&gt;</span>
    <span class="kw">&lt;dependencies&gt;</span>
        <span class="cm">&lt;!-- Driver oficial de PostgreSQL JDBC --&gt;</span>
        <span class="kw">&lt;dependency&gt;</span>
            <span class="kw">&lt;groupId&gt;</span>org.postgresql<span class="kw">&lt;/groupId&gt;</span>
            <span class="kw">&lt;artifactId&gt;</span>postgresql<span class="kw">&lt;/artifactId&gt;</span>
            <span class="kw">&lt;version&gt;</span><span class="str">42.7.2</span><span class="kw">&lt;/version&gt;</span>
        <span class="kw">&lt;/dependency&gt;</span>

        <span class="cm">&lt;!-- Hibernate ORM Core 6 (Implementación de Jakarta Persistence API) --&gt;</span>
        <div class="hl-block"><span class="kw">&lt;dependency&gt;</span>
            <span class="kw">&lt;groupId&gt;</span>org.hibernate.orm<span class="kw">&lt;/groupId&gt;</span>
            <span class="kw">&lt;artifactId&gt;</span>hibernate-core<span class="kw">&lt;/artifactId&gt;</span>
            <span class="kw">&lt;version&gt;</span><span class="str">6.4.4.Final</span><span class="kw">&lt;/version&gt;</span>
        <span class="kw">&lt;/dependency&gt;</span></div>

        <span class="kw">&lt;dependency&gt;</span>
            <span class="kw">&lt;groupId&gt;</span>junit<span class="kw">&lt;/groupId&gt;</span>
            <span class="kw">&lt;artifactId&gt;</span>junit<span class="kw">&lt;/artifactId&gt;</span>
            <span class="kw">&lt;version&gt;</span><span class="str">3.8.1</span><span class="kw">&lt;/version&gt;</span>
            <span class="kw">&lt;scope&gt;</span>test<span class="kw">&lt;/scope&gt;</span>
        <span class="kw">&lt;/dependency&gt;</span>
    <span class="kw">&lt;/dependencies&gt;</span>
</pre>
"""
render_html_to_png(
    wrap_ide_window("Configuración de Dependencias Maven", "pom.xml", html_pom, breadcrumbs="Examen", status_text="Maven: 3.9.16 | Hibernate 6.4.4.Final"),
    os.path.join(CAPTURES_DIR, "03_estructura_proyecto_pom.png"),
    height=540
)

# -------------------------------------------------------------
# 4. hibernate.cfg.xml
# -------------------------------------------------------------
html_cfg = """
<pre>
<span class="kw">&lt;hibernate-configuration&gt;</span>
    <span class="kw">&lt;session-factory&gt;</span>
        <span class="cm">&lt;!-- 1. Propiedades de conexión a PostgreSQL --&gt;</span>
        <span class="kw">&lt;property</span> <span class="var">name</span>=<span class="str">"connection.driver_class"</span><span class="kw">&gt;</span>org.postgresql.Driver<span class="kw">&lt;/property&gt;</span>
        <span class="kw">&lt;property</span> <span class="var">name</span>=<span class="str">"connection.url"</span><span class="kw">&gt;</span>jdbc:postgresql://localhost:5432/hangar_imperio_db<span class="kw">&lt;/property&gt;</span>
        <span class="kw">&lt;property</span> <span class="var">name</span>=<span class="str">"connection.username"</span><span class="kw">&gt;</span>antonio<span class="kw">&lt;/property&gt;</span>
        <span class="kw">&lt;property</span> <span class="var">name</span>=<span class="str">"connection.password"</span><span class="kw">&gt;</span>admin<span class="kw">&lt;/property&gt;</span>

        <span class="cm">&lt;!-- 2. Dialecto SQL para Hibernate 6 --&gt;</span>
        <span class="kw">&lt;property</span> <span class="var">name</span>=<span class="str">"dialect"</span><span class="kw">&gt;</span>org.hibernate.dialect.PostgreSQLDialect<span class="kw">&lt;/property&gt;</span>

        <span class="cm">&lt;!-- 3. Depuración e inspección de queries SQL generadas --&gt;</span>
        <span class="kw">&lt;property</span> <span class="var">name</span>=<span class="str">"show_sql"</span><span class="kw">&gt;</span>true<span class="kw">&lt;/property&gt;</span>
        <span class="kw">&lt;property</span> <span class="var">name</span>=<span class="str">"format_sql"</span><span class="kw">&gt;</span>true<span class="kw">&lt;/property&gt;</span>
        <span class="kw">&lt;property</span> <span class="var">name</span>=<span class="str">"hbm2ddl.auto"</span><span class="kw">&gt;</span>update<span class="kw">&lt;/property&gt;</span>

        <span class="cm">&lt;!-- 4. Registro de Entidades Persistentes --&gt;</span>
        <div class="hl-block"><span class="kw">&lt;mapping</span> <span class="var">class</span>=<span class="str">"org.dam.accesodatos.ut4.examen.models.Nave"</span><span class="kw">/&gt;</span>
        <span class="kw">&lt;mapping</span> <span class="var">class</span>=<span class="str">"org.dam.accesodatos.ut4.examen.models.CazaLigero"</span><span class="kw">/&gt;</span>
        <span class="kw">&lt;mapping</span> <span class="var">class</span>=<span class="str">"org.dam.accesodatos.ut4.examen.models.DestructorEstelar"</span><span class="kw">/&gt;</span>
        <span class="kw">&lt;mapping</span> <span class="var">class</span>=<span class="str">"org.dam.accesodatos.ut4.examen.models.Planeta"</span><span class="kw">/&gt;</span></div>
    <span class="kw">&lt;/session-factory&gt;</span>
<span class="kw">&lt;/hibernate-configuration&gt;</span>
</pre>
"""
render_html_to_png(
    wrap_ide_window("Descriptor de Configuración Hibernate", "hibernate.cfg.xml", html_cfg, breadcrumbs="src/main/resources", status_text="XML Schema Validated"),
    os.path.join(CAPTURES_DIR, "04_configuracion_hibernate.png"),
    height=640
)

# -------------------------------------------------------------
# 5. Entidad Planeta.java
# -------------------------------------------------------------
html_planeta = """
<pre>
<span class="kw">package</span> org.dam.accesodatos.ut4.examen.models;

<span class="kw">import</span> jakarta.persistence.*;
<span class="kw">import</span> org.hibernate.annotations.ColumnDefault;

<div class="hl-block"><span class="ann">@Entity</span>
<span class="ann">@Table</span>(<span class="var">name</span> = <span class="str">"planetas"</span>)
<span class="kw">public class</span> <span class="cls">Planeta</span> {</div>
    <span class="ann">@Id</span>
    <span class="ann">@GeneratedValue</span>(<span class="var">strategy</span> = <span class="cls">GenerationType</span>.<span class="var">IDENTITY</span>)
    <span class="ann">@Column</span>(<span class="var">name</span> = <span class="str">"planeta_id"</span>)
    <span class="kw">private</span> <span class="cls">Integer</span> <span class="var">id</span>;

    <span class="ann">@Column</span>(<span class="var">name</span> = <span class="str">"nombre"</span>, <span class="var">nullable</span> = <span class="kw">false</span>, <span class="var">unique</span> = <span class="kw">true</span>, <span class="var">length</span> = <span class="num">100</span>)
    <span class="kw">private</span> <span class="cls">String</span> <span class="var">nombre</span>;

    <span class="ann">@Column</span>(<span class="var">name</span> = <span class="str">"clima"</span>, <span class="var">length</span> = <span class="num">50</span>)
    <span class="kw">private</span> <span class="cls">String</span> <span class="var">clima</span>;

    <span class="ann">@Column</span>(<span class="var">name</span> = <span class="str">"afiliacion"</span>, <span class="var">length</span> = <span class="num">50</span>)
    <span class="ann">@ColumnDefault</span>(<span class="str">"'NEUTRAL'"</span>)
    <span class="kw">private</span> <span class="cls">String</span> <span class="var">afiliacion</span>;

    <span class="kw">public</span> <span class="fn">Planeta</span>() {}
    <span class="cm">// Constructores, Getters y Setters...</span>
}
</pre>
"""
render_html_to_png(
    wrap_ide_window("Entidad Planeta", "Planeta.java", html_planeta, breadcrumbs="models", status_text="Jakarta Persistence 3.1"),
    os.path.join(CAPTURES_DIR, "05_entidad_planeta.png"),
    height=600
)

# -------------------------------------------------------------
# 6. Clase Base Abstracta Nave.java (SINGLE_TABLE)
# -------------------------------------------------------------
html_nave = """
<pre>
<span class="kw">package</span> org.dam.accesodatos.ut4.examen.models;

<span class="kw">import</span> jakarta.persistence.*;
<span class="kw">import</span> java.io.Serializable;

<div class="hl-block"><span class="ann">@Entity</span>
<span class="ann">@Table</span>(<span class="var">name</span> = <span class="str">"naves"</span>)
<span class="ann">@Inheritance</span>(<span class="var">strategy</span> = <span class="cls">InheritanceType</span>.<span class="var">SINGLE_TABLE</span>) <span class="cm">// Estrategia Tabla Única</span>
<span class="ann">@DiscriminatorColumn</span>(<span class="var">name</span> = <span class="str">"tipo_nave"</span>, <span class="var">discriminatorType</span> = <span class="cls">DiscriminatorType</span>.<span class="var">STRING</span>)
<span class="kw">public abstract class</span> <span class="cls">Nave</span> <span class="kw">implements</span> <span class="cls">Serializable</span> {</div>

    <span class="ann">@Id</span>
    <span class="ann">@GeneratedValue</span>(<span class="var">strategy</span> = <span class="cls">GenerationType</span>.<span class="var">IDENTITY</span>)
    <span class="ann">@Column</span>(<span class="var">name</span> = <span class="str">"nave_id"</span>)
    <span class="kw">private int</span> <span class="var">id</span>;

    <span class="ann">@Column</span>(<span class="var">name</span> = <span class="str">"nombre"</span>, <span class="var">nullable</span> = <span class="kw">false</span>, <span class="var">length</span> = <span class="num">100</span>)
    <span class="kw">private</span> <span class="cls">String</span> <span class="var">nombre</span>;

    <span class="ann">@Column</span>(<span class="var">name</span> = <span class="str">"modelo"</span>, <span class="var">length</span> = <span class="num">50</span>, <span class="var">nullable</span> = <span class="kw">false</span>)
    <span class="kw">private</span> <span class="cls">String</span> <span class="var">modelo</span>;

    <span class="ann">@Column</span>(<span class="var">name</span> = <span class="str">"estado_sistema"</span>, <span class="var">nullable</span> = <span class="kw">false</span>, <span class="var">length</span> = <span class="num">20</span>)
    <span class="kw">private</span> <span class="cls">String</span> <span class="var">estadoSistema</span>;

    <div class="hl-block"><span class="cm">// Relación ManyToOne Perezosa (LAZY) hacia Planeta</span>
    <span class="ann">@ManyToOne</span>(<span class="var">fetch</span> = <span class="cls">FetchType</span>.<span class="var">LAZY</span>)
    <span class="ann">@JoinColumn</span>(<span class="var">name</span> = <span class="str">"planeta_origen_id"</span>)
    <span class="kw">private</span> <span class="cls">Planeta</span> <span class="var">planetaOrigen</span>;</div>
}
</pre>
"""
render_html_to_png(
    wrap_ide_window("Mapeo Jerárquico Tabla Única", "Nave.java", html_nave, breadcrumbs="models", status_text="InheritanceType.SINGLE_TABLE"),
    os.path.join(CAPTURES_DIR, "06_jerarquia_nave_abstracta.png"),
    height=670
)

# -------------------------------------------------------------
# 7. Subclases Polimórficas (CazaLigero & DestructorEstelar)
# -------------------------------------------------------------
html_subclasses = """
<pre>
<span class="cm">// Subclase 1: CazaLigero (Discriminador: CAZA)</span>
<span class="ann">@Entity</span>
<div class="hl-block"><span class="ann">@DiscriminatorValue</span>(<span class="str">"CAZA"</span>)
<span class="kw">public class</span> <span class="cls">CazaLigero</span> <span class="kw">extends</span> <span class="cls">Nave</span> {
    <span class="ann">@Column</span>(<span class="var">name</span> = <span class="str">"potencia_fuego"</span>)
    <span class="kw">private</span> <span class="cls">Integer</span> <span class="var">potenciaFuego</span>;
    <span class="cm">// Constructores, Getters y Setters...</span>
}</div>

<span class="cm">// Subclase 2: DestructorEstelar (Discriminador: DESTRUCTOR)</span>
<span class="ann">@Entity</span>
<div class="hl-block"><span class="ann">@DiscriminatorValue</span>(<span class="str">"DESTRUCTOR"</span>)
<span class="kw">public class</span> <span class="cls">DestructorEstelar</span> <span class="kw">extends</span> <span class="cls">Nave</span> {
    <span class="ann">@Column</span>(<span class="var">name</span> = <span class="str">"capacidad_escudos"</span>)
    <span class="kw">private int</span> <span class="var">capacidadEscudos</span>;
    <span class="cm">// Constructores, Getters y Setters...</span>
}</div>
</pre>
"""
render_html_to_png(
    wrap_ide_window("Subclases Especializadas con Discriminador", "CazaLigero.java / DestructorEstelar.java", html_subclasses, breadcrumbs="models", status_text="@DiscriminatorValue CAZA & DESTRUCTOR"),
    os.path.join(CAPTURES_DIR, "07_subclases_polimorficas.png"),
    height=550
)

# -------------------------------------------------------------
# 8. Desafío 1: Sensor de Escuadrones Polimórfico (INNER JOIN + TYPE)
# -------------------------------------------------------------
html_d1 = """
<pre>
<span class="cm">/**
 * Desafío 1: Retorna únicamente instancias reales de CazaLigero filtradas por bando
 * omitiendo cazas en estado 'Mantenimiento'. Utiliza la función TYPE(n).
 */</span>
<span class="kw">public</span> <span class="cls">List</span>&lt;<span class="cls">CazaLigero</span>&gt; <span class="fn">obtenerCazasOperativosPorBando</span>(<span class="cls">String</span> <span class="var">bando</span>) {
    <span class="kw">try</span> (<span class="cls">Session</span> <span class="var">session</span> = <span class="cls">HibernateUtil</span>.<span class="fn">getSessionFactory</span>().<span class="fn">openSession</span>()) {

        <div class="hl-block"><span class="cls">String</span> <span class="var">hql</span> = <span class="str">"SELECT n FROM CazaLigero n "</span> +
                     <span class="str">"INNER JOIN n.planetaOrigen p "</span> +
                     <span class="str">"WHERE TYPE(n) = CazaLigero "</span> +
                     <span class="str">"AND p.afiliacion = :bando "</span> +
                     <span class="str">"AND n.estadoSistema &lt;&gt; :estadoMantenimiento"</span>;</div>

        <span class="cls">Query</span>&lt;<span class="cls">CazaLigero</span>&gt; <span class="var">query</span> = <span class="var">session</span>.<span class="fn">createQuery</span>(<span class="var">hql</span>, <span class="cls">CazaLigero</span>.<span class="kw">class</span>);
        <span class="var">query</span>.<span class="fn">setParameter</span>(<span class="str">"bando"</span>, <span class="var">bando</span>);
        <span class="var">query</span>.<span class="fn">setParameter</span>(<span class="str">"estadoMantenimiento"</span>, <span class="str">"Mantenimiento"</span>);

        <span class="kw">return</span> <span class="var">query</span>.<span class="fn">list</span>();
    } <span class="kw">catch</span> (<span class="cls">Exception</span> <span class="var">e</span>) {
        <span class="cls">System</span>.<span class="var">err</span>.<span class="fn">println</span>(<span class="str">"❌ Error al consultar cazas: "</span> + <span class="var">e</span>.<span class="fn">getMessage</span>());
        <span class="kw">return</span> <span class="cls">Collections</span>.<span class="fn">emptyList</span>();
    }
}
</pre>
"""
render_html_to_png(
    wrap_ide_window("Desafío 1 - HQL con TYPE(n) e INNER JOIN", "HoloNetService.java", html_d1, breadcrumbs="services", status_text="HQL Polimórfico | TYPE(n)"),
    os.path.join(CAPTURES_DIR, "08_desafio1_hql_type.png"),
    height=600
)

# -------------------------------------------------------------
# 9. Desafío 2: Mitigación N+1 (FETCH JOIN)
# -------------------------------------------------------------
html_d2 = """
<pre>
<span class="cm">/**
 * Desafío 2: Recupera todas las naves en estado 'Critico' (polimorfismo sobre Nave).
 * Evita el problema de rendimiento N+1 forzando la carga inmediata del planeta
 * mediante la cláusula INNER JOIN FETCH.
 */</span>
<span class="kw">public</span> <span class="cls">List</span>&lt;<span class="cls">Nave</span>&gt; <span class="fn">obtenerFlotaCriticaPolimorfica</span>() {
    <span class="kw">try</span> (<span class="cls">Session</span> <span class="var">session</span> = <span class="cls">HibernateUtil</span>.<span class="fn">getSessionFactory</span>().<span class="fn">openSession</span>()) {

        <div class="hl-block"><span class="cls">String</span> <span class="var">hql</span> = <span class="str">"FROM Nave n "</span> +
                     <span class="str">"INNER JOIN FETCH n.planetaOrigen p "</span> +
                     <span class="str">"WHERE n.estadoSistema = :estadoCritico"</span>;</div>

        <span class="cls">Query</span>&lt;<span class="cls">Nave</span>&gt; <span class="var">query</span> = <span class="var">session</span>.<span class="fn">createQuery</span>(<span class="var">hql</span>, <span class="cls">Nave</span>.<span class="kw">class</span>);
        <span class="var">query</span>.<span class="fn">setParameter</span>(<span class="str">"estadoCritico"</span>, <span class="str">"Critico"</span>);

        <span class="kw">return</span> <span class="var">query</span>.<span class="fn">list</span>();
    } <span class="kw">catch</span> (<span class="cls">Exception</span> <span class="var">e</span>) {
        <span class="cls">System</span>.<span class="var">err</span>.<span class="fn">println</span>(<span class="str">"❌ Error al obtener flota: "</span> + <span class="var">e</span>.<span class="fn">getMessage</span>());
        <span class="kw">return</span> <span class="cls">Collections</span>.<span class="fn">emptyList</span>();
    }
}
</pre>
"""
render_html_to_png(
    wrap_ide_window("Desafío 2 - Mitigación del Problema N+1 con FETCH JOIN", "HoloNetService.java", html_d2, breadcrumbs="services", status_text="Eager Fetching HQL"),
    os.path.join(CAPTURES_DIR, "09_desafio2_hql_fetch_join.png"),
    height=580
)

# -------------------------------------------------------------
# 10. Desafío 3: Proyecciones Planas de Inteligencia (LEFT JOIN)
# -------------------------------------------------------------
html_d3 = """
<pre>
<span class="cm">/**
 * Desafío 3: Reporte plano tabular optimizado proyectando [nombre, tipo_nave, planeta].
 * Utiliza LEFT JOIN estándar (sin fetch) para incluir naves que no tengan planeta
 * asignado (mostrando null).
 */</span>
<span class="kw">public</span> <span class="cls">List</span>&lt;<span class="cls">Object</span>[]&gt; <span class="fn">obtenerReporteGeneralFiltrado</span>() {
    <span class="kw">try</span> (<span class="cls">Session</span> <span class="var">session</span> = <span class="cls">HibernateUtil</span>.<span class="fn">getSessionFactory</span>().<span class="fn">openSession</span>()) {

        <div class="hl-block"><span class="cls">String</span> <span class="var">hql</span> = <span class="str">"SELECT n.nombre, TYPE(n), p.nombre "</span> +
                     <span class="str">"FROM Nave n "</span> +
                     <span class="str">"LEFT JOIN n.planetaOrigen p"</span>;</div>

        <span class="cls">Query</span>&lt;<span class="cls">Object</span>[]&gt; <span class="var">query</span> = <span class="var">session</span>.<span class="fn">createQuery</span>(<span class="var">hql</span>, <span class="cls">Object</span>[].<span class="kw">class</span>);

        <span class="kw">return</span> <span class="var">query</span>.<span class="fn">list</span>();
    } <span class="kw">catch</span> (<span class="cls">Exception</span> <span class="var">e</span>) {
        <span class="cls">System</span>.<span class="var">err</span>.<span class="fn">println</span>(<span class="str">"❌ Error al generar reporte: "</span> + <span class="var">e</span>.<span class="fn">getMessage</span>());
        <span class="kw">return</span> <span class="cls">Collections</span>.<span class="fn">emptyList</span>();
    }
}
</pre>
"""
render_html_to_png(
    wrap_ide_window("Desafío 3 - Proyección Escalar y LEFT JOIN", "HoloNetService.java", html_d3, breadcrumbs="services", status_text="Scalar Projection | List<Object[]>"),
    os.path.join(CAPTURES_DIR, "10_desafio3_hql_proyeccion.png"),
    height=580
)

# -------------------------------------------------------------
# 11. Ejecución y Salida por Consola de MainHangar
# -------------------------------------------------------------
html_exec = """
<pre>
<span class="t-cyan">=== INICIO PRUEBAS ===</span>
<span class="t-green">✔ [HibernateUtil] SessionFactory inicializada correctamente en el sector.</span>

<span class="t-yellow">--- 1. Obtener Cazas Operativos Por Bando ---</span>
<span class="t-dim">Hibernate: select cl1_0.nave_id, cl1_0.estado_sistema, cl1_0.modelo, cl1_0.nombre, cl1_0.potencia_fuego
           from naves cl1_0 join planetas po1_0 on po1_0.planeta_id=cl1_0.planeta_origen_id
           where 'CAZA'='CAZA' and po1_0.afiliacion=? and cl1_0.estado_sistema&lt;&gt;? and cl1_0.tipo_nave='CAZA'</span>
     <span class="t-white">Cazas Bando NEUTRAL :</span>          <span class="t-dim">(0 resultados: Halcón Milenario está en 'Mantenimiento' -&gt; Filtrado)</span>
     <span class="t-white">Cazas Bando IMPERIO :</span>
         <span class="t-cyan">CazaLigero{potenciaFuego=40}</span>      <span class="t-dim">(Caza TIE Alfa, Coruscant, 'Critico')</span>
     <span class="t-white">Cazas Bando ALIANZA REBELDE :</span>
         <span class="t-cyan">CazaLigero{potenciaFuego=85}</span>      <span class="t-dim">(Caza X-Wing, Yavin IV, 'Estable')</span>

<span class="t-yellow">--- 2. Obtener Flota Crítica Polimórfica (FETCH JOIN Anti N+1) ---</span>
<span class="t-dim">Hibernate: select n1_0.nave_id, n1_0.tipo_nave, n1_0.estado_sistema, n1_0.modelo, n1_0.nombre,
                  po1_0.planeta_id, po1_0.afiliacion, po1_0.clima, po1_0.nombre,
                  n1_0.potencia_fuego, n1_0.capacidad_escudos
           from naves n1_0 join planetas po1_0 on po1_0.planeta_id=n1_0.planeta_origen_id
           where n1_0.estado_sistema=?</span>
     <span class="t-purple">DestructorEstelar{capacidadEscudos=45000}</span>  <span class="t-dim">(Superdestructor Ejecutor, Coruscant)</span>
     <span class="t-cyan">CazaLigero{potenciaFuego=40}</span>              <span class="t-dim">(Caza TIE Alfa, Coruscant)</span>

<span class="t-yellow">--- 3. Obtener Reporte General (Proyección Escalar + LEFT JOIN) ---</span>
<span class="t-dim">Hibernate: select n1_0.nombre, n1_0.tipo_nave, po1_0.nombre
           from naves n1_0 left join planetas po1_0 on po1_0.planeta_id=n1_0.planeta_origen_id</span>
     <span class="t-green">[Caza X-Wing, class org.dam.accesodatos.ut4.examen.models.CazaLigero, Yavin IV]</span>
     <span class="t-green">[Destructor Estelar, class org.dam.accesodatos.ut4.examen.models.DestructorEstelar, Coruscant]</span>
     <span class="t-green">[Superdestructor Ejecutor, class org.dam.accesodatos.ut4.examen.models.DestructorEstelar, Coruscant]</span>
     <span class="t-green">[Caza TIE Alfa, class org.dam.accesodatos.ut4.examen.models.CazaLigero, Coruscant]</span>
     <span class="t-green">[Halcón Milenario, class org.dam.accesodatos.ut4.examen.models.CazaLigero, Tatooine]</span>

<span class="t-dim">ℹ [HibernateUtil] SessionFactory cerrada de forma segura.</span>
<span class="t-cyan">=== FIN DE LA EJECUCIÓN ===</span>
<span class="t-green">[INFO] BUILD SUCCESS</span>
</pre>
"""
render_html_to_png(
    wrap_terminal_window("Terminal de Ejecución - MainHangar Verificación de Resultados", "mvn exec:java -Dexec.mainClass=\"org.dam.accesodatos.ut4.examen.MainHangar\"", html_exec, height=720),
    os.path.join(CAPTURES_DIR, "11_ejecucion_main_resultados.png"),
    height=740
)

print("Todas las capturas se han generado exitosamente en:", CAPTURES_DIR)
