rule auto_rule_20250726160106_5600 {
  strings:
    $o0 = "DllMain" wide ascii nocase
    $o1 = "x6C642E6C" wide ascii nocase
    $o2 = "configure_narrow_argv" wide ascii nocase
    $o3 = "dword_10004040" wide ascii nocase
  condition:
    4 of ($o*)
}