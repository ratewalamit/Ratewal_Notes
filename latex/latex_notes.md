﻿
 #Latex Notes


**install latex**
```shell
sudo apt-get install texlive-full
```
**Compile with latex**
```
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
``` 
**latexdiff**
```shell
#to create latexdiff you need to first compile with pdflatex as descrived above then
latexdiff-vc --pdf --revision d2950d2c32 Paper.tex
```
 
**insert figure**
```
\begin{figure}[h!]       h! ensures figure at specific location
\begin{center}

\includegraphics[width=\linewidth,keepaspectratio]{history_of_universe.png}
\end{center}
\end{figure}
```
or    
```
\usepackage{lipsum}
\usepackage{graphicx}
\usepackage{transparent}
\usepackage{eso-pic}
\AddToShipoutPicture*{
    \put(0,0){
        \parbox[b][\paperheight]{\paperwidth}{%
            \vfill
            \centering
            \includegraphics[width=0.5\textwidth]{drawing}%
            \vfill
        }
    }
    \put(0,0){%
        \transparent{0.7}\textcolor{white}{\rule{\paperwidth}{\paperheight}}
    }
}
```



**figure and text side by side**

```
\documentclass{article}
\usepackage{graphicx,wrapfig,lipsum}
%------------------------------------------
\begin{document}
This is where the table goes with text wrapping around it. You may 
embed tabular environment inside wraptable environment and customize as you like.
%------------------------------------------
\setlength{\intextsep}{20pt}
\setlength{\columnsep}{20pt}
\begin{wrapfigure}{r}{5.5cm}
\caption{A wrapped figure going nicely inside the text.}\label{wrap-fig:1}
\includegraphics[width=5.5cm]{sample}
\end{wrapfigure} 
%------------------------------------------
{\lipsum[2-3]
\par
Figure~\ref{wrap-fig:1} is a wrapped figure.
%------------------------------------------
\end{document}

\noindent   for wrap figure text without indetation
```


**hpace*

hspace*{0.5cm}  for after newline spacing   
```
#newline
\\[0.5cm]      newline after 0.5cm of vsapce
iography}
#bibliography
```

**citatinos**
```
\usepackage{natbib}
\bibliographystyle{abbrvnat}
\setcitestyle{authoryear,open={(},close={)}}
#
\citet{Charles85}
\citep{Charles85}


\citep{Lacey93,Lacey94,Giocoli07}   # Lacay&Cole 1993,1994; Giocoli 2007
 ```
 
**bibliography**

```
\bibitem[Lacey \& Cole(1993)]{Lacey93}
Lacey C., Cole S., 1993, MNRAS, 262, 627
\bibitem[Lacey \& Cole(1994)]{Lacey94}
Lacey C., Cole S., 1994, MNRAS, 271, 676


\begin{thebibliography}{9}
\bibitem[Charles,Subu, 1985]{Charles85}
Albert Einstein. 
\textit{Zur Elektrodynamik
bewegeter K {\"o}rper}.
(German)
[\textbf{On electrodynaimics of moving objects}].
Annalen der Physik,322(10):891-921.

\end{thebibliography}
```





**Symbols outside math mode:**

< >   \textless   \textgreater

 ~ \textasciitilde



**writign equations** 

```
\begin{align*}
    \Large
    \Delta \Sigma (R)   \equiv \left\langle \gamma_t \right\rangle \Sigma_{crit}= \overline{\Sigma(<R)} -  \left\langle \Sigma(R)\right\rangle 
    \vspace{1cm}
    
   \Delta \Sigma(R)=   \Delta \Sigma_{parent}(R|Rsat) +  \Delta \Sigma_{satellite}(R) + \Delta \Sigma_{stellar}(R)
   \vspace{1cm}
   
   \Delta \Sigma_{parent}(R)  = \frac{\displaystyle\int_{0}^{2\pi} \Delta \Sigma(r) \cos(2\alpha)  d\theta }{\displaystyle 2\pi}     %Note \distplastyle effect
 \vspace{1cm}
   
 
 \overline{\Delta \Sigma}(R) = \frac{      \displaystyle\int  n(R_{\rm sat})  \Delta \Sigma(R|R_{\rm sat})  dR_{\rm sat}   }{ \displaystyle\int  n(R_{\rm sat})   dR_{\rm sat} }
   \vspace{1cm} 
     
\end{align*}\newline
```

