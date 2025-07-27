rule auto_rule_20250726104840_6563 {
  strings:
    $o0 = "x7562CC9392EF84LL" wide ascii nocase
    $o1 = "x7299CDBC98FBFELL" wide ascii nocase
    $o2 = "x180000000uLL" wide ascii nocase
    $o3 = "dword_1802881B0" wide ascii nocase
  condition:
    4 of ($o*)
}