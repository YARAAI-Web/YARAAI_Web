rule auto_rule_20250726160055_0635 {
  strings:
    $o0 = "off_46E760" wide ascii nocase
    $o1 = "dword_46E280" wide ascii nocase
    $o2 = "lStart" wide ascii nocase
    $o3 = "__freetlocinfo" wide ascii nocase
  condition:
    4 of ($o*)
}