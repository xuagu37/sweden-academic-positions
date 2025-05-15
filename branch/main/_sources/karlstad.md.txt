# Karlstad University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 11</p>


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

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in Media and Communication Studies</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:806004/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 18.May.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Engelsk titel</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:808988/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 20.May.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Biblioteksvärdar till Universitetsbiblioteket</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:822821/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 20.May.2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in Computer Science, 6G-NTN mobile systems</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:781427/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 21.May.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Internrevisionschef</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:822499/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 21.May.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Universitetsadjunkt i företagsekonomi med inriktning mot industriell ekonomi</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:826050/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 25.May.2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD position in Computer Science, TRUMAN</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:788719/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 29.May.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Universitetsadjunkt i företagsekonomi med inriktning mot marknadsföring</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:826166/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 31.May.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>The project has no title</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:800023/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 05.Jun.2025

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Senior Lecturer in Computer Science, Specialisation in AI Engineering</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:718619/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 08.Jun.2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in civil law</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:811193/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 10.Jun.2025
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
