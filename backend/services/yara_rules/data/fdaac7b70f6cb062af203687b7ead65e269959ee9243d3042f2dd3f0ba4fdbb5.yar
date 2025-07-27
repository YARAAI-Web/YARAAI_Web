rule auto_rule_20250726151735_7417 {
  strings:
    $o0 = "dword_4040F0" wide ascii nocase
    $o1 = "byte_40405E" wide ascii nocase
    $o2 = "dword_404197" wide ascii nocase
    $o3 = "dword_4041C6" wide ascii nocase
  condition:
    4 of ($o*)
}