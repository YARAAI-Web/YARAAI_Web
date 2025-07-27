rule auto_rule_20250726094706_5962 {
  strings:
    $o0 = "GetCursorPos" wide ascii nocase
    $o1 = "ExceptionPtr" wide ascii nocase
    $o2 = "qword_140003958" wide ascii nocase
    $o3 = "dword_140005660" wide ascii nocase
    $o4 = "physical" wide ascii nocase
  condition:
    4 of ($o*)
}