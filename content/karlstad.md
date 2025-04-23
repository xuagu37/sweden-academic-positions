# Karlstad University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 10</p>


<div id="filters" style="margin: 1em 0;">
  <label for="filterType"><strong>Filter by Job Type:</strong></label>
  <select id="filterType" style="margin-right: 1em;">
    <option value="">Show All</option>
    <option value="PhD">PhD</option>
    <option value="Postdoc/Researcher">Postdoc/Researcher</option>
    <option value="Lecturer/Professor">Lecturer/Professor</option>
    <option value="Research Engineer">Research Engineer</option>    
    <option value="Other">Other</option>
  </select>
  <input type="text" id="jobFilter" placeholder="Search jobs..." style="padding: 0.5em; width: 50%;">
</div>

<div id="jobList">
<div class="job" data-type="None" style="margin-bottom: 1.5em;">

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Utbildningshandläggare, vikariat 100 %</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:813022/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 23.Apr.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Nordisk gästforskare i socialt arbete till FoU Välfärd Värmland</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:801169/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 25.Apr.2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in English with a specialisation in English literature</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:795758/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 28.Apr.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Doktorand i biologi med avslutning licentiatexamen</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:804400/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 29.Apr.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Amanuenser i datavetenskap</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:811114/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 29.Apr.2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in Environmental and Energy Systems</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:793079/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 04.May.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Doktorand i folkhälsovetenskap, inriktning oral hälsa</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:799415/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 04.May.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Fakultetsadministratör 75%</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:817989/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 05.May.2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral Student in Biology</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:812910/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 08.May.2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in Media and Communication Studies</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:806004/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 18.May.2025
</div></div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const typeSelect = document.getElementById('filterType');
  const textInput = document.getElementById('jobFilter');
  const jobBlocks = document.querySelectorAll('.job');

  function updateDisplay() {
    const selected = typeSelect.value.toLowerCase();
    const query = textInput.value.toLowerCase();

    jobBlocks.forEach(job => {
      const jobType = (job.dataset.type || "").toLowerCase();
      const matchesType = !selected || jobType === selected;
      const matchesQuery = job.textContent.toLowerCase().includes(query);
      job.style.display = (matchesType && matchesQuery) ? '' : 'none';
    });
  }

  typeSelect.addEventListener('change', updateDisplay);
  textInput.addEventListener('input', updateDisplay);
});
</script>
