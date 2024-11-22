
<link rel="stylesheet" href="mystyle.css">

<h1>My First CSS Example</h1>
<p>This is a paragraph.</p>

<div>
  It **works!**<br>
  It **works!**
</div>


<style>red { color: red }</style>
<red>This is a paragraph.</red>



<span style="color:blue">some *This is Blue italic.* text</span>

<font color='red'>test blue color font</font>
$${\color{red}Red}$$
$\color{blue}{your-text-here}$

\documentclass{article}
\usepackage[most]{tcolorbox}

\tcbset{
    frame code={},
    center title,
    left=0pt,
    right=0pt,
    top=0pt,
    bottom=0pt,
    colback=gray!70,
    colframe=white,
    width=\dimexpr\textwidth\relax,
    enlarge left by=0mm,
    boxsep=5pt,
    arc=0pt,outer arc=0pt,
    }

\begin{document}
\begin{tcolorbox}
\textsc{Extra Curricular Achievements}
\end{tcolorbox}
\end{document}
