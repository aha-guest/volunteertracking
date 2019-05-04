module.exports = {
  opportunities: {
    url: '/api/opportunities',
    text: ({ name, partner_name }) => {
      return `${name} - ${partner_name}`;
    },
    rows: [[{
      label: 'Partner',
      name: 'partner_name',
    }], [{
      label: 'Address',
      name: 'location_street'
    }, {
      label: 'City',
      name: 'location_city'
    }], [{
      label: 'State',
      name: 'location_state',
      value: 'CO',
      disabled: true
    }, {
      label: 'Zip',
      name: 'location_zip',
      type: 'number'
    }], [{
      label: 'Opportunity Name',
      name: 'name'
    }], [{
      label: 'Shift Hours',
      name: 'shift_hours',
      type: 'number'
    }], [{
      label: 'Start Date',
      name: 'start_date',
      type: 'date',
      optional: true
    }, {
      label: 'End Date',
      name: 'end_date',
      type: 'date',
      optional: true
    }], [{
      label: 'Commitment Length',
      ex: 'days',
      name: 'commitment_length',
      type: 'number',
      optional: true
    }], [{
      label: 'Frequency',
      ex: 'Eg. "Every other Friday"',
      name: 'frequency',
      optional: true
    }], [{
      label: 'Training Required',
      ex: '(hours)',
      name: 'training_time_required',
      type: 'number',
      optional: true
    }], [{
      label: 'Volunteers Needed',
      name: 'volunteers_needed',
      type: 'number',
      optional: true
    }], [{
      label: 'Tags',
      ex: 'Eg. "children, art"',
      name: 'tags_string',
      placeholder: 'Enter Tags (Eg. children, art, games)',
      optional: true
    }], [{
      label: 'Description',
      name: 'description',
      type: 'textarea'
    }]]
  },
  partners: {
    url: '/api/partners',
    text: ({name, job_count}) => {
      return `${name} - ${job_count} Jobs`;
    },
    rows: [[{
      label: 'Partner Name',
      name: 'name'
    }]]
  }
};