rule auto_rule_20250726102214_7371 {
  strings:
    $o0 = "dword_40E020" wide ascii nocase
    $o1 = "_byte_0" wide ascii nocase
    $o2 = "LibraryA" wide ascii nocase
    $o3 = "_except_handler3" wide ascii nocase
    $o4 = "dword_411B30" wide ascii nocase
  condition:
    4 of ($o*)
}