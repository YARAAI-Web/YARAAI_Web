rule auto_rule_20250726135336_5711 {
  strings:
    $o0 = "dword_43776B" wide ascii nocase
    $o1 = "x5314u" wide ascii nocase
    $o2 = "x75108B5" wide ascii nocase
  condition:
    3 of ($o*)
}