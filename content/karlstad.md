# Karlstad University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 6</p>


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
<h3>Universitetsadjunkt i socialt arbete, vikariat</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:870565/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 27.Nov.2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in Media and Communication Studies</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:868905/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 30.Nov.2025

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral Researcher in Computer Science, High-Quality Synthetic Data</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:822730/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 30.Nov.2025

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral researcher in chemistry with a focus on sustainable production of cellulose fibers</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:874336/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 03.Dec.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Projektassistent i biologi med fokus på ekologisk modellering av strömfiskpopulationer</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:872208/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 03.Dec.2025

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Senior lecturer in Criminal Law</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:856591/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 14.Dec.2025
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
