rule auto_rule_20250726200818_7258 {
  strings:
    $o0 = "qword_140041F40" wide ascii nocase
    $o1 = "Only" wide ascii nocase
    $o2 = "_pyinstaller_pyz" wide ascii nocase
  condition:
    3 of ($o*)
}