rule auto_rule_20250726190658_2406 {
  strings:
    $o0 = "setbuf" wide ascii nocase
    $o1 = "PyUnicode_AsUTF8" wide ascii nocase
    $o2 = "qword_140042E18" wide ascii nocase
    $o3 = "qword_140042DC8" wide ascii nocase
  condition:
    4 of ($o*)
}