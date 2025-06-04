/*
  Warnings:

  - You are about to drop the `assignment` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE `assignment` DROP FOREIGN KEY `Assignment_instructor_id_fkey`;

-- DropTable
DROP TABLE `assignment`;
