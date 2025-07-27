rule auto_rule_20250727030330_6025 {
  strings:
    $o0 = "wsprintfW" wide ascii nocase
    $o1 = "x7FEEu" wide ascii nocase
    $o2 = "qword_42E6F3" wide ascii nocase
    $o3 = "x5EA20000693ELL" wide ascii nocase
    $o4 = "dword_42FD86" wide ascii nocase
  condition:
    4 of ($o*)
}