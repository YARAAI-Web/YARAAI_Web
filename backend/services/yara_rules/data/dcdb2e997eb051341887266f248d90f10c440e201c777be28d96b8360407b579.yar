rule auto_rule_20250726080352_4118 {
  strings:
    $o0 = "_mm_xor_si128" wide ascii nocase
    $o1 = "xmmword_11FA9CD0" wide ascii nocase
    $o2 = "dword_12130A10" wide ascii nocase
  condition:
    3 of ($o*)
}