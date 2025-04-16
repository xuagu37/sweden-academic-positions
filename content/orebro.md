# Örebro University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 4</p>


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
<h3>Doctoral student in Computer Science (Machine Learning)</h3>

<ul>
  <li><strong>Link:</strong> <a href="https://www.oru.se/english/career/available-positions/job/?jid=20250051">View job posting</a></li>
  <li><strong>Department:</strong> </li>
  <li><strong>Published:</strong> </li>
  <li><strong>Deadline:</strong> 2025-04-28</li>
</ul>

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor of Sport Science</h3>

<ul>
  <li><strong>Link:</strong> <a href="https://www.oru.se/english/career/available-positions/job/?jid=20250079">View job posting</a></li>
  <li><strong>Department:</strong> </li>
  <li><strong>Published:</strong> </li>
  <li><strong>Deadline:</strong> 2025-04-28</li>
</ul>

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Senior lecturer in criminology</h3>

<ul>
  <li><strong>Link:</strong> <a href="https://www.oru.se/english/career/available-positions/job/?jid=20250099">View job posting</a></li>
  <li><strong>Department:</strong> </li>
  <li><strong>Published:</strong> </li>
  <li><strong>Deadline:</strong> 2025-05-07</li>
</ul>

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral researcher in Biomedicine</h3>

<ul>
  <li><strong>Link:</strong> <a href="https://www.oru.se/english/career/available-positions/job/?jid=20250078">View job posting</a></li>
  <li><strong>Department:</strong> </li>
  <li><strong>Published:</strong> </li>
  <li><strong>Deadline:</strong> 2025-05-15</li>
</ul>
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
