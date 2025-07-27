rule auto_rule_20250726220151_7485 {
  strings:
    $o0 = "byte_460624" wide ascii nocase
    $o1 = "dword_46062C" wide ascii nocase
    $o2 = "_commit" wide ascii nocase
    $o3 = "lpCharType" wide ascii nocase
    $o4 = "SetStdHandle" wide ascii nocase
  condition:
    4 of ($o*)
}