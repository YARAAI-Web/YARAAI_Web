rule auto_rule_20250727024747_5397 {
  strings:
    $o0 = "v257" wide ascii nocase
    $o1 = "dword_73954" wide ascii nocase
    $o2 = "dword_7389C" wide ascii nocase
    $o3 = "dword_73404" wide ascii nocase
    $o4 = "dword_737A4" wide ascii nocase
  condition:
    4 of ($o*)
}