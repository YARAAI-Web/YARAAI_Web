rule auto_rule_20250726140714_2161 {
  strings:
    $o0 = "x6E62BAA2" wide ascii nocase
    $o1 = "dword_1401FD534" wide ascii nocase
    $o2 = "dword_1401FD5E0" wide ascii nocase
    $o3 = "dword_1401FD548" wide ascii nocase
  condition:
    4 of ($o*)
}