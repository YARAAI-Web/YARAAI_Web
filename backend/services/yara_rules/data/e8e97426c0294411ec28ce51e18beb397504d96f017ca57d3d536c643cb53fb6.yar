rule auto_rule_20250726151542_1207 {
  strings:
    $o0 = "p_hWnd" wide ascii nocase
    $o1 = "dword_4C12F8" wide ascii nocase
    $o2 = "iswspace" wide ascii nocase
    $o3 = "Script" wide ascii nocase
  condition:
    4 of ($o*)
}