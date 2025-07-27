rule auto_rule_20250726224217_9044 {
  strings:
    $o0 = "Tcl_MutexLock" wide ascii nocase
    $o1 = "absolute" wide ascii nocase
    $o2 = "Py_ExitStatusException" wide ascii nocase
    $o3 = "qword_140042F80" wide ascii nocase
  condition:
    4 of ($o*)
}