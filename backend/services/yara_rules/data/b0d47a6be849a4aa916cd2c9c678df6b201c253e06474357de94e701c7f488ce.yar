rule auto_rule_20250726163548_5535 {
  strings:
    $o0 = "qword_180003B30" wide ascii nocase
    $o1 = "x180001C46LL" wide ascii nocase
    $o2 = "x180002172LL" wide ascii nocase
    $o3 = "dword_180005618" wide ascii nocase
    $o4 = "_stdio_common_vfprintf" wide ascii nocase
  condition:
    4 of ($o*)
}