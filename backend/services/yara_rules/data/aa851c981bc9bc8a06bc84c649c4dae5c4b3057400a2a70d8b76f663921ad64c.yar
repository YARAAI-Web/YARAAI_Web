rule auto_rule_20250726172408_5384 {
  strings:
    $o0 = "dword_45CC18" wide ascii nocase
    $o1 = "strpbrk" wide ascii nocase
    $o2 = "off_45C920" wide ascii nocase
    $o3 = "dword_45CDA4" wide ascii nocase
  condition:
    4 of ($o*)
}