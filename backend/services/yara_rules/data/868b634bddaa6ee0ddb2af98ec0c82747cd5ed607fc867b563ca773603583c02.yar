rule auto_rule_20250726195556_0246 {
  strings:
    $o0 = "FindExSearchNameMatch" wide ascii nocase
    $o1 = "Only" wide ascii nocase
    $o2 = "Tcl_ConditionNotify" wide ascii nocase
    $o3 = "qword_14003ECF0" wide ascii nocase
  condition:
    4 of ($o*)
}