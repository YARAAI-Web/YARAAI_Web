rule auto_rule_20250726195943_5331 {
  strings:
    $o0 = "iswspace" wide ascii nocase
    $o1 = "dword_4C12C4" wide ascii nocase
    $o2 = "x50B008C4u" wide ascii nocase
    $o3 = "dword_4C116C" wide ascii nocase
    $o4 = "x312u" wide ascii nocase
  condition:
    4 of ($o*)
}