/*
  Warnings:

  - You are about to drop the column `duration` on the `session` table. All the data in the column will be lost.
  - You are about to drop the column `instructor_id` on the `session` table. All the data in the column will be lost.
  - You are about to drop the column `is_live` on the `session` table. All the data in the column will be lost.
  - You are about to drop the column `start_time` on the `session` table. All the data in the column will be lost.
  - Added the required column `deadline` to the `Session` table without a default value. This is not possible if the table is not empty.
  - Added the required column `instructor` to the `Session` table without a default value. This is not possible if the table is not empty.
  - Added the required column `meeting_link` to the `Session` table without a default value. This is not possible if the table is not empty.
  - Added the required column `unit_name` to the `Session` table without a default value. This is not possible if the table is not empty.
  - Added the required column `user_id` to the `Session` table without a default value. This is not possible if the table is not empty.
  - Made the column `description` on table `session` required. This step will fail if there are existing NULL values in that column.

*/
-- DropIndex
DROP INDEX `session_instructor_idx` ON `session`;

-- AlterTable
ALTER TABLE `session` DROP COLUMN `duration`,
    DROP COLUMN `instructor_id`,
    DROP COLUMN `is_live`,
    DROP COLUMN `start_time`,
    ADD COLUMN `deadline` DATETIME(3) NOT NULL,
    ADD COLUMN `instructor` VARCHAR(120) NOT NULL,
    ADD COLUMN `meeting_link` VARCHAR(255) NOT NULL,
    ADD COLUMN `unit_name` VARCHAR(120) NOT NULL,
    ADD COLUMN `user_id` VARCHAR(120) NOT NULL,
    MODIFY `description` VARCHAR(255) NOT NULL;

-- CreateIndex
CREATE INDEX `session_user_idx` ON `Session`(`user_id`);
