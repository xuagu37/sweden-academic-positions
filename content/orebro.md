# Örebro University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 2</p>


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
<h3>Doctoral student in legal science with a focus on Regulation of AI</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250228)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-01

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in Computer Science with a focus on embodied learning</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250251)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-18
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
