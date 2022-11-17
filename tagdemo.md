curl -X POST -k -H 'Content-Type:application/json' -u admin:Ansible123 -d '{"job_tags": "wasrestart","limit": "server2,server3"}' https://192.168.1.160/api/v2/job_templates/tag-demo/launch/
