rule auto_rule_20250726183018_9650 {
  strings:
    $o0 = "qword_140037D18" wide ascii nocase
    $o1 = "setbuf" wide ascii nocase
    $o2 = "PyLong_AsLong" wide ascii nocase
    $o3 = "qword_140044EC0" wide ascii nocase
  condition:
    4 of ($o*)
}