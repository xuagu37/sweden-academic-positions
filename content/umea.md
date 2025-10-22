# Umeå University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 12</p>


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

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor in Computing Science with a focus on Software Engineering</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/professor-in-computing-science-with-a-focus-on-software-engineering_857018/)
- **Department:** Department of Computing Science
- **Published:** 
- **Deadline:** 2025-10-27

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Two PhD positions in Medical Science with orientation to Molecular Biology</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/two-phd-positions-in-medical-science-with-orientation-to-molecular-biology_857832/)
- **Department:** Department of Molecular Biology
- **Published:** 
- **Deadline:** 2025-10-29

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctor (2 years) in Organic Electronics with focus on the development of a novel light-emission technology</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/postdoctor-2-years-in-organic-electronics-with-focus-on-the-development-of-a-novel-light-emission-technology_852955/)
- **Department:** Department of Physics
- **Published:** 
- **Deadline:** 2025-10-31

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD-student</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/phd-student-_856371/)
- **Department:** Department of Chemistry
- **Published:** 
- **Deadline:** 2025-10-31

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD position in Medical Science with orientation towards Molecular Biology</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/phd-position-in-medical-science-with-orientation-towards-molecular-biology_867515/)
- **Department:** Department of Molecular Biology
- **Published:** 
- **Deadline:** 2025-11-12

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral position: Studying Climate Change with plant ecophysiology</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/postdoctoral-position-studying-climate-change-with-plant-ecophysiology_825481/)
- **Department:** Department of Medical Biochemistry and Biophysics
- **Published:** 
- **Deadline:** 2025-11-13

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD position in Computational Physics – Simulation Intelligence</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/phd-position-in-computational-physics--simulation-intelligence_858914/)
- **Department:** Department of Physics
- **Published:** 
- **Deadline:** 2025-11-15

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Assistant professor of Data driven Precision Medicine and Diagnostics</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/assistant-professor-of-data-driven-precision-medicine-and-diagnostics_855584/)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-11-15

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>1-2 PhD students for the Department of Political Science</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/1-2-phd-students-for-the-department-of-political-science_860718/)
- **Department:** Department of Political Science
- **Published:** 
- **Deadline:** 2025-11-16

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Computing Science with a focus on Neuro-Symbolic Graph Transformation</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/phd-student-in-computing-science-with-a-focus-on-neuro-symbolic-graph-transformation_867087/)
- **Department:** Department of Computing Science
- **Published:** 
- **Deadline:** 2025-11-23

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral position in statistics</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/postdoctoral-position-in-statistics_861332/)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-11-30

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Post doctor (2 years) within “Embodied-AI and Human-Robot-Interaction”</h3>

- **Link:** [View job posting](https://www.umu.se/en/work-with-us/open-positions/post-doctor-2-years-within-embodied-ai-and-human-robot-interaction_867301/)
- **Department:** Department of Computing Science
- **Published:** 
- **Deadline:** 2025-11-30
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
