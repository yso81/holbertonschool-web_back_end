export default function getListStudentIds (arrayOfIds) {
    if (!Array.isArray(arrayOfIds)) {
        return [];
    }
    return arrayOfIds.map((student) => student.id);
}