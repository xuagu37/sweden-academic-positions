# Stockholm University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 14</p>


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
<h3>PhD student in Neurochemistry with molecular neurobiology</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:833275/where:4/)
- **Department:** Department of Biochemistry and Biophysics
- **Published:** 
- **Deadline:** 2025-08-20

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Researcher in Quantum Field Theory</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:846607/where:4/)
- **Department:** Nordic Institute for Theoretical Physics (NORDITA)
- **Published:** 
- **Deadline:** 2025-08-21

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral Fellow to project INSPIRI</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:834041/where:4/)
- **Department:** Stockholm Resilience Centre
- **Published:** 
- **Deadline:** 2025-08-31

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Associate Professor in Experimental Chemical Physics with focus on X-Ray Characterization of Chemical Processes</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:827506/where:4/)
- **Department:** Department of Physics
- **Published:** 
- **Deadline:** 2025-09-01

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Bioinformatician at NGI</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:847632/where:4/)
- **Department:** Department of Biochemistry and Biophysics
- **Published:** 
- **Deadline:** 2025-09-01

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Criminology</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:831893/where:4/)
- **Department:** Department of Criminology
- **Published:** 
- **Deadline:** 2025-09-01

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Assistant professor in Materials Chemistry with focus on Computational Materials Design</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:815120/where:4/)
- **Department:** Department of Chemistry
- **Published:** 
- **Deadline:** 2025-09-01

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Staff Scientist within Scanning Electron Microcopy (SEM)</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:842202/where:4/)
- **Department:** Department of Chemistry
- **Published:** 
- **Deadline:** 2025-09-01

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Bioinformaticians at NBIS</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:847098/where:4/)
- **Department:** Department of Biochemistry and Biophysics
- **Published:** 
- **Deadline:** 2025-09-05

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Associate Professor in Radiation Biology with Focus on Molecular Mechanisms</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:835631/where:4/)
- **Department:** Department of Molecular Biosciences, The Wenner-Gren Institute
- **Published:** 
- **Deadline:** 2025-09-08

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Metamorphic petrology</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:833906/where:4/)
- **Department:** Department of Geological Sciences
- **Published:** 
- **Deadline:** 2025-09-08

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Bioinformatics</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:830925/where:4/)
- **Department:** Department of Biochemistry and Biophysics
- **Published:** 
- **Deadline:** 2025-09-15

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Computer and Systems Sciences, with focus on Enterprise Architecture and Digital Transformation</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:839736/where:4/)
- **Department:** Department of Computer and Systems Sciences
- **Published:** 
- **Deadline:** 2025-10-15

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral Fellow in Theoretical Physics</h3>

- **Link:** [View job posting](https://su.varbi.com/what:job/jobID:821810/where:4/)
- **Department:** Nordic Institute for Theoretical Physics (NORDITA)
- **Published:** 
- **Deadline:** 2025-10-31
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
