<h1>Glitch FX 2 (WIP)</h1>
<h2>The 'sequel' to my first GlitchFX generator!</h2>
<p>This project is still a work in progress, but I'm slowly working to add new filters, and improve the documentation.</p>
<h3>Steps to get started</h3>
<ul>
<li>This program uses opencv with python, which requires at Python version 3.6 or higher, and pip 19.3 or higher</li>
<li>When downloaded/cloned from the repo, navigate to the root directory ("/glitch-fx") and install the necessary dependencies with: <pre><code>pip install -r requirements.txt</code></pre>After everything is installed, run the main script by typing:<pre><code>python glitchfx2</code></pre>into the command line.</li><li>Running this program for the first time will create a "src" folder if not already created, for you to store your images in at the root folder ("/glitch-fx/src").</li>
<li>With a source folder in place, running the above script again should lead to the following prompt: <pre><code>Choose an input image file:</code></pre>where you input the filename of any image in the "src" folder</li>
<li>A recurring prompt will be shown afterwards saying <pre><code>Enter an effect ~ x to finish:</code></pre> exactly what it sounds like. You can refer to the tables below, but the input will be in the following format:<pre><code>effectname parameter value</code></pre>Example: <pre><code>noisy -p 0.2</code></pre>
</li>
<li>When done, press 'x' to exit and display the result</li>
</ul>
<h3>List of operations</h3>
<table>
    <tr>
        <th>Operation</th>
        <th>Available Parameters</th>
    </tr>
    <tr><td>noisy</td><td>-p</td></tr>
    <tr><td>scanline</td><td>-or</td></tr>
    <tr><td>highpass</td><td>-p, -k, -a</td></tr>
    <tr><td>scanner</td><td>-s, -e, -or</td></tr>
    <tr><td>burn</td><td>-p</td></tr>
    <tr><td>warp</td><td>-t, -f</td></tr>
    <tr><td>random shift</td><td>-p, -s, -e</td>
</table>
<h3>Description of Parameters</h3>
<table>
    <tr>
        <th>Parameter</th>
        <th>Full Name</th>
        <th>Expected Input</th>
    </tr>
    <tr>
        <td>-p</td>
        <td>percent</td>
        <td>A normalized float value between 0.0 and 1.0</td>
    </tr>
    <tr>
        <td>-or</td>
        <td>orientation</td>
        <td>h or v (for 'horizontal' or 'vertical')</td>
    </tr>
    <tr>
        <td>-k</td>
        <td>kernel size</td>
        <td>An odd integer greater than 1 (3,5,7,...)</td>
    </tr>
    <tr>
        <td>-a</td>
        <td>amplitude</td>
        <td>Any number value</td>
    </tr>
    <tr>
        <td>-s</td>
        <td>start</td>
        <td>A normalized float value between 0.0 and 1.0</td>
    </tr>
    <tr>
        <td>-e</td>
        <td>end</td>
        <td>A normalized float value between 0.0 and 1.0 <strong>(but greater than -s)</strong></td>
    </tr>
    <tr>
        <td>-t</td>
        <td>type (of warp)</td>
        <td>shearX shearY rotateX or rotateY</td>
    </tr>
    <tr>
        <td>-f</td>
        <td>factor</td>
        <td>Any number value</td>
    </tr>
</table>
