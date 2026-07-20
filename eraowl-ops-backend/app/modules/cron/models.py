# Cron module — scheduled job metadata lives in the 'cron' PostgreSQL schema
# (owned by postgres). No SQLModel entities are mirrored here in this pilot;
# this module exposes a lightweight status endpoint for the scheduler service.
