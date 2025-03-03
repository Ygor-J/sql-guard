CREATE OR REPLACE TABLE `central-rampart-451901-k9.test.student`(name STRING, age INT, major STRING, semester STRING, course STRING, grade FLOAT64, failed BOOL)
AS SELECT * FROM (
    SELECT 'John Doe' AS name, 20 AS age, 'Computer Science' AS major, '1S/2024' AS semester, 'Algorithms' AS course, 8.5 AS grade, FALSE AS failed,
    UNION ALL
    SELECT 'Jane Smith', 21, 'Computer Science', '1S/2024', 'Data Structures', 7.0, FALSE,
    UNION ALL
    SELECT 'Alice Johnson', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 5.5, TRUE
    UNION ALL
    SELECT 'Bob Brown', 19, 'Computer Science', '1S/2024', 'Algorithms', 4.0, TRUE
    UNION ALL
    SELECT 'Charlie Davis', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 9.0, FALSE
    UNION ALL
    SELECT 'Diana Evans', 21, 'Computer Science', '1S/2024', 'Data Structures', 6.5, TRUE
    UNION ALL
    SELECT 'Ethan Green', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 8.0, FALSE
    UNION ALL
    SELECT 'Fiona Harris', 19, 'Computer Science', '1S/2024', 'Algorithms', 7.5, FALSE
    UNION ALL
    SELECT 'George Clark', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 3.5, TRUE
    UNION ALL
    SELECT 'Hannah Lewis', 21, 'Computer Science', '1S/2024', 'Data Structures', 9.5, FALSE
    UNION ALL
    SELECT 'Ian Walker', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 6.0, TRUE
    UNION ALL
    SELECT 'Jessica Hall', 19, 'Computer Science', '1S/2024', 'Algorithms', 8.0, FALSE
    UNION ALL
    SELECT 'Kevin Young', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 7.0, FALSE
    UNION ALL
    SELECT 'Laura Allen', 21, 'Computer Science', '1S/2024', 'Data Structures', 5.0, TRUE
    UNION ALL
    SELECT 'Michael King', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 9.5, FALSE
    UNION ALL
    SELECT 'Natalie Wright', 19, 'Computer Science', '1S/2024', 'Algorithms', 6.5, TRUE
    UNION ALL
    SELECT 'Oscar Scott', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 8.5, FALSE
    UNION ALL
    SELECT 'Paula Adams', 21, 'Computer Science', '1S/2024', 'Data Structures', 7.5, FALSE
    UNION ALL
    SELECT 'Quincy Baker', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 4.5, TRUE
    UNION ALL
    SELECT 'Rachel Carter', 19, 'Computer Science', '1S/2024', 'Algorithms', 9.0, FALSE
    UNION ALL
    SELECT 'Samuel Perez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 6.0, TRUE
    UNION ALL
    SELECT 'Tina Turner', 21, 'Computer Science', '1S/2024', 'Data Structures', 8.0, FALSE
    UNION ALL
    SELECT 'Ulysses White', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 7.5, FALSE
    UNION ALL
    SELECT 'Victoria Harris', 19, 'Computer Science', '1S/2024', 'Algorithms', 5.5, TRUE
    UNION ALL
    SELECT 'Walter Martinez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 9.5, FALSE
    UNION ALL
    SELECT 'Xena Lopez', 21, 'Computer Science', '1S/2024', 'Data Structures', 6.5, TRUE
    UNION ALL
    SELECT 'Yara Gonzalez', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 8.0, FALSE
    UNION ALL
    SELECT 'Zackary Hill', 19, 'Computer Science', '1S/2024', 'Algorithms', 7.0, FALSE
    UNION ALL
    SELECT 'Amelia Green', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 4.0, TRUE
    UNION ALL
    SELECT 'Benjamin Adams', 21, 'Computer Science', '1S/2024', 'Data Structures', 9.0, FALSE
    UNION ALL
    SELECT 'Chloe Baker', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 5.0, TRUE
    UNION ALL
    SELECT 'Daniel Carter', 19, 'Computer Science', '1S/2024', 'Algorithms', 8.5, FALSE
    UNION ALL
    SELECT 'Ella Perez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 7.5, FALSE
    UNION ALL
    SELECT 'Finn Turner', 21, 'Computer Science', '1S/2024', 'Data Structures', 6.0, TRUE
    UNION ALL
    SELECT 'Grace White', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 9.5, FALSE
    UNION ALL
    SELECT 'Henry Harris', 19, 'Computer Science', '1S/2024', 'Algorithms', 5.5, TRUE
    UNION ALL
    SELECT 'Isabella Martinez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 8.0, FALSE
    UNION ALL
    SELECT 'Jack Lopez', 21, 'Computer Science', '1S/2024', 'Data Structures', 7.0, FALSE
    UNION ALL
    SELECT 'Katie Gonzalez', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 6.5, TRUE
    UNION ALL
    SELECT 'Liam Hill', 19, 'Computer Science', '1S/2024', 'Algorithms', 9.0, FALSE
    UNION ALL
    SELECT 'Mia Green', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 4.5, TRUE
    UNION ALL
    SELECT 'Noah Adams', 21, 'Computer Science', '1S/2024', 'Data Structures', 8.5, FALSE
    UNION ALL
    SELECT 'Olivia Baker', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 7.5, FALSE
    UNION ALL
    SELECT 'Parker Carter', 19, 'Computer Science', '1S/2024', 'Algorithms', 6.0, TRUE
    UNION ALL
    SELECT 'Quinn Perez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 9.0, FALSE
    UNION ALL
    SELECT 'Riley Turner', 21, 'Computer Science', '1S/2024', 'Data Structures', 5.0, TRUE
    UNION ALL
    SELECT 'Sophia White', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 8.0, FALSE
    UNION ALL
    SELECT 'Thomas Harris', 19, 'Computer Science', '1S/2024', 'Algorithms', 7.5, FALSE
    UNION ALL
    SELECT 'Uma Martinez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 6.5, TRUE
    UNION ALL
    SELECT 'Victor Lopez', 21, 'Computer Science', '1S/2024', 'Data Structures', 9.5, FALSE
    UNION ALL
    SELECT 'Wendy Gonzalez', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 4.0, TRUE
    UNION ALL
    SELECT 'Xander Hill', 19, 'Computer Science', '1S/2024', 'Algorithms', 8.0, FALSE
    UNION ALL
    SELECT 'Yara Green', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 7.0, FALSE
    UNION ALL
    SELECT 'Zane Adams', 21, 'Computer Science', '1S/2024', 'Data Structures', 6.0, TRUE
    UNION ALL
    SELECT 'Ava Baker', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 9.0, FALSE
    UNION ALL
    SELECT 'Blake Carter', 19, 'Computer Science', '1S/2024', 'Algorithms', 5.5, TRUE
    UNION ALL
    SELECT 'Cora Perez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 8.5, FALSE
    UNION ALL
    SELECT 'Dylan Turner', 21, 'Computer Science', '1S/2024', 'Data Structures', 7.5, FALSE
    UNION ALL
    SELECT 'Eva White', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 6.5, TRUE
    UNION ALL
    SELECT 'Felix Harris', 19, 'Computer Science', '1S/2024', 'Algorithms', 9.5, FALSE
    UNION ALL
    SELECT 'Gina Martinez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 5.0, TRUE
    UNION ALL
    SELECT 'Hank Lopez', 21, 'Computer Science', '1S/2024', 'Data Structures', 8.0, FALSE
    UNION ALL
    SELECT 'Ivy Gonzalez', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 7.0, FALSE
    UNION ALL
    SELECT 'Jake Hill', 19, 'Computer Science', '1S/2024', 'Algorithms', 6.5, TRUE
    UNION ALL
    SELECT 'Kara Green', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 9.0, FALSE
    UNION ALL
    SELECT 'Leo Adams', 21, 'Computer Science', '1S/2024', 'Data Structures', 5.5, TRUE
    UNION ALL
    SELECT 'Maya Baker', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 8.5, FALSE
    UNION ALL
    SELECT 'Nate Carter', 19, 'Computer Science', '1S/2024', 'Algorithms', 7.0, FALSE
    UNION ALL
    SELECT 'Olive Perez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 6.0, TRUE
    UNION ALL
    SELECT 'Peyton Turner', 21, 'Computer Science', '1S/2024', 'Data Structures', 9.0, FALSE
    UNION ALL
    SELECT 'Quincy White', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 4.5, TRUE
    UNION ALL
    SELECT 'Rory Harris', 19, 'Computer Science', '1S/2024', 'Algorithms', 8.0, FALSE
    UNION ALL
    SELECT 'Sadie Martinez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 7.5, FALSE
    UNION ALL
    SELECT 'Tyler Lopez', 21, 'Computer Science', '1S/2024', 'Data Structures', 6.5, TRUE
    UNION ALL
    SELECT 'Uma Gonzalez', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 9.5, FALSE
    UNION ALL
    SELECT 'Violet Hill', 19, 'Computer Science', '1S/2024', 'Algorithms', 5.0, TRUE
    UNION ALL
    SELECT 'Wyatt Green', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 8.0, FALSE
    UNION ALL
    SELECT 'Xander Adams', 21, 'Computer Science', '1S/2024', 'Data Structures', 7.0, FALSE
    UNION ALL
    SELECT 'Yara Baker', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 6.0, TRUE
    UNION ALL
    SELECT 'Zoe Carter', 19, 'Computer Science', '1S/2024', 'Algorithms', 9.0, FALSE
    UNION ALL
    SELECT 'Aaron Perez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 5.5, TRUE
    UNION ALL
    SELECT 'Bella Turner', 21, 'Computer Science', '1S/2024', 'Data Structures', 8.5, FALSE
    UNION ALL
    SELECT 'Caleb White', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 7.5, FALSE
    UNION ALL
    SELECT 'Daisy Harris', 19, 'Computer Science', '1S/2024', 'Algorithms', 6.0, TRUE
    UNION ALL
    SELECT 'Eli Martinez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 9.0, FALSE
    UNION ALL
    SELECT 'Fiona Lopez', 21, 'Computer Science', '1S/2024', 'Data Structures', 5.0, TRUE
    UNION ALL
    SELECT 'Gavin Gonzalez', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 8.0, FALSE
    UNION ALL
    SELECT 'Hazel Hill', 19, 'Computer Science', '1S/2024', 'Algorithms', 7.0, FALSE
    UNION ALL
    SELECT 'Ivy Green', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 6.5, TRUE
    UNION ALL
    SELECT 'Jasper Adams', 21, 'Computer Science', '1S/2024', 'Data Structures', 9.5, FALSE
    UNION ALL
    SELECT 'Kylie Baker', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 4.0, TRUE
    UNION ALL
    SELECT 'Liam Carter', 19, 'Computer Science', '1S/2024', 'Algorithms', 8.5, FALSE
    UNION ALL
    SELECT 'Mila Perez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 7.5, FALSE
    UNION ALL
    SELECT 'Nora Turner', 21, 'Computer Science', '1S/2024', 'Data Structures', 6.0, TRUE
    UNION ALL
    SELECT 'Owen White', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 9.0, FALSE
    UNION ALL
    SELECT 'Penny Harris', 19, 'Computer Science', '1S/2024', 'Algorithms', 5.5, TRUE
    UNION ALL
    SELECT 'Quinn Martinez', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 8.0, FALSE
    UNION ALL
    SELECT 'Ryan Lopez', 21, 'Computer Science', '1S/2024', 'Data Structures', 7.0, FALSE
    UNION ALL
    SELECT 'Sofia Gonzalez', 22, 'Electrical Engineering', '1S/2024', 'Calculus I', 6.5, TRUE
    UNION ALL
    SELECT 'Theo Hill', 19, 'Computer Science', '1S/2024', 'Algorithms', 9.0, FALSE
    UNION ALL
    SELECT 'Uma Green', 20, 'Electrical Engineering', '1S/2024', 'Circuit Analysis', 5.0, TRUE
    UNION ALL
    SELECT 'Violet Adams', 21, 'Computer Science', '1S/2024', 'Data Structures', 8.5, FALSE
    UNION ALL
    SELECT 'Wyatt Baker', 22, 'Electrical Engineering', '1S/2024', 'Calculus II', 7.5, FALSE
)
