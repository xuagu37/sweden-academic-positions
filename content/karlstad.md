# Karlstad University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 9</p>


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
<h3>Projektassistent, forskning inom folkhälsovetenskap</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:836531/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 03.Jul.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Universitetsadjunkter i omvårdnad</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:835735/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 03.Aug.2025

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral position in Computer Science, OPEHRA</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:822208/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 03.Aug.2025

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctor in Risk and Environmental Studies with a focus on disaster risk management and the effects of risk reducing efforts</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:838171/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 10.Aug.2025

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Associate senior lecturer in Analytical chemistry with expertise in chromatography</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:793503/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 17.Aug.2025

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Associate senior lecturer in Biochemistry</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:793506/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 17.Aug.2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Engelsk titel</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:837792/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 31.Aug.2025

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor i litteraturvetenskap</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:835444/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 31.Oct.2025

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor i engelska med litteraturvetenskaplig inriktning</h3>

- **Link:** [View job posting](https://kau.varbi.com/en/what:job/jobID:835449/iframeEmbedded:0/where:4)
- **Department:** 
- **Published:** 
- **Deadline:** 31.Oct.2025
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
