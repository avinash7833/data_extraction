from django.shortcuts import render
from .forms import UploadPDFForm
from .pdf_extraction_script import extract_data_from_pdf
from .models import ExtractedData  # Import the ExtractedData model

def upload_pdf(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            extracted_data = extract_data_from_pdf(pdf_file)
            
            invoice_number = extracted_data.get("Invoice Number")
            
            extracted_data_obj = ExtractedData.objects.create(
                invoice_number=invoice_number,
                date=extracted_data.get("Date"),
                total_amount=extracted_data.get("Total Amount")
            )
            return render(request, 'result.html', {'data': extracted_data_obj})
    else:
        form = UploadPDFForm()
    return render(request, 'upload.html', {'form': form})
