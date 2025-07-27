rule auto_rule_20250726131424_2274 {
  strings:
    $o0 = "Tcl_SetVar2Ex" wide ascii nocase
    $o1 = "dwInitParam" wide ascii nocase
    $o2 = "qword_140042E58" wide ascii nocase
    $o3 = "dword_14003FD10" wide ascii nocase
  condition:
    4 of ($o*)
}