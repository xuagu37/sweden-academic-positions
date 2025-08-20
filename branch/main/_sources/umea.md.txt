# Umeå University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 13</p>


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

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral researcher in Sociology with a focus on Waste Studies</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/postdoctoral-researcher-in-sociology-with-a-focus-on-waste-studies_840738/)
- **Department:** Department of Sociology
- **Published:** 
- **Deadline:** 2025-08-22

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor of Philosophy</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/professor-of-philosophy_822386/)
- **Department:** Department of Historical, Philosophical and Religious Studies
- **Published:** 
- **Deadline:** 2025-08-29

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Staff scientist in Bioinformatics and Data Science</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/staff-scientist-in-bioinformatics-and-data-science_838707/)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-31

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD-student</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/phd-student-_848320/)
- **Department:** Department of Psychology
- **Published:** 
- **Deadline:** 2025-08-31

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Staff Scientist - AI factory (two positions)</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/staff-scientist---ai-factory-two-positions_848498/)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-05

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Teaching assistants to Umeå School of Architecture</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/teaching-assistants-to-umea-school-of-architecture_840630/)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-07

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD position in structural biology of virus replication</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/phd-position-in-structural-biology-of-virus-replication_847969/)
- **Department:** Department of Medical Biochemistry and Biophysics
- **Published:** 
- **Deadline:** 2025-09-07

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Staff scientist with focus on AI trustworthiness modeling in human-robot interactions</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/staff-scientist-with-focus-on-ai-trustworthiness-modeling-in-human-robot-interactions_836992/)
- **Department:** Department of Computing Science
- **Published:** 
- **Deadline:** 2025-09-10

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Staff scientist</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/staff-scientist_832051/)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-12

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD-student in Computing Science with focus on Computer Security</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/phd-student-in-computing-science-with-focus-on-computer-security_848581/)
- **Department:** Department of Computing Science
- **Published:** 
- **Deadline:** 2025-09-12

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor in Fine Arts</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/professor-in-fine-arts_818703/)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-30

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD-student in Sociology</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/phd-student-in-sociology_840856/)
- **Department:** Department of Sociology
- **Published:** 
- **Deadline:** 2025-10-15

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral fellow in neurophysiology</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/postdoctoral-fellow-in-neurophysiology_848918/)
- **Department:** Department of Medical and Translational Biology
- **Published:** 
- **Deadline:** 2025-10-17
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
