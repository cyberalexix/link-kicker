-- upgrade --
ALTER TABLE "user" ALTER COLUMN "hour" TYPE JSONB USING CASE WHEN "hour" IS NULL THEN jsonb_build_array() ELSE jsonb_build_array("hour") END;
-- downgrade --
ALTER TABLE "user" ALTER COLUMN "hour" TYPE SMALLINT USING NULLIF("hour"[0], 'null')::SMALLINT;
